import cv2
import redis
import base64
import numpy as np
import os
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier('face.xml')
temp_db=redis.Redis()
while True:
    state,frame=cap.read()
    if(state==True):
        # cv2.imshow('frame',frame)
        #encode 
        gray_scale =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(frame,scaleFactor=1.2,minNeighbors=5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,128),3)
            cv2.rectangle(gray_scale,(x,y),(x+w,y+h),(0,0,0),3)

        _,Colord_Buffred_Frame=cv2.imencode('.jpg',frame)
        _,Gray_Bufferd_Frame=cv2.imencode('.jpg',gray_scale)
        colord_jpg_as_text = base64.b64encode(Gray_Bufferd_Frame)
        gray_jpg_as_text=base64.b64encode(Colord_Buffred_Frame)

        temp_db.set('colord',colord_jpg_as_text)
        temp_db.set('colord_id',os.urandom(4))
        temp_db.set('gary',gray_jpg_as_text)
        temp_db.set('gray_id',os.urandom(4))
        #decode

        jpg_as_buffer_from_colord =base64.b64decode(colord_jpg_as_text)
        jpg_as_buffer_from_gray=base64.b64decode(gray_jpg_as_text)

        jpg_as_np_from_colord = np.frombuffer(jpg_as_buffer_from_colord, dtype=np.uint8)
        jpg_as_np_from_buffred = np.frombuffer(jpg_as_buffer_from_gray, dtype=np.uint8)
        
        image_buffer_from_colord = cv2.imdecode(jpg_as_np_from_colord, flags=1)
        image_buffer_from_gray=cv2.imdecode(jpg_as_np_from_buffred,flags=1)
        print('Colored =>',image_buffer_from_colord)
        print('Gray =>',image_buffer_from_gray)
        
        cv2.imshow('Stream Colored',image_buffer_from_colord)
        cv2.imshow('Stream Gray',image_buffer_from_gray)
       
        if (cv2.waitKey(1) & 0xFF == ord('q')):
             break
cap.release()
cv2.destroyAllWindows()