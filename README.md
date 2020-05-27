# PYCCTV
Webcam over WebSocket using OpenCV and Tornado With Nigth Vison Mode(grayscale) and Light Mode And Face Reacognation

-----------------------------------

# setup:
<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/https://github.com/MedAmineFouzai/PYCCTV </td>
</tr>
<tr>
<td> 2) cd PYCCTV</td>
</tr>
<tr>
<td> 3) pip install pipenv</td>
</tr>
</tr>
<td> 4) pipenv --python 3.6</td>
</tr>
<tr>
<td> 5) pipenv install - r requirements.txt</td>
</tr>
<tr>
  <td>
    6) run project with <a href="https://pypi.org/project/torn/">torn cli</a> : <b>#command: [ torn run ] </b>  </td>
 </tr>
</table>

----------------------------------------

# Theory:
the purpose of this project is to mimic a cctv over network using websocket protocol with web technologies.
A CCTV  pick up the images, which are then transmitted then to a recording device and then a monitor in this case the webcam well save the images with the help of opencv then saving it to redis and send it via tornado server to a real time show on te browser.

this kind of way called a MJPEG Stream

# Technologies:

<h3>Redis:</h3>
<img src="https://cdn4.iconfinder.com/data/icons/redis-2/1451/Untitled-2-512.png" widht='300' height='300'>
Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broke


<h3>OpenCV:</h3>

<img src="https://github.com/MedAmineFouzai/PYCCTV/blob/master/Captures/opencv-logo.png">
<h4>OpenCV is a library of programming functions mainly aimed at real-time computer vision and highly optimized .</h4>


 # Resualt:
<h3>Motion MJPEG</h3>
In multimedia, Motion JPEG (M-JPEG or MJPEG) is a video compression format in which each video frame or interlaced field of a digital video sequence is compressed separately as a JPEG image

-----------------------------------------

## For Future Usage:
the "video" is streamd via a html "img" tag ☺ it would be grate if i cant do the same with audio
