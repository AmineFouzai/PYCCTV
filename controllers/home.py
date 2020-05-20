
'''
Preset controller by torn for / route
'''
from .modules import *
#note do same to audio
class homeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class stream_request_handler(tornado.websocket.WebSocketHandler):
    
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self._store=redis.Redis()
        self.colored_prev_id=None
        self.gray_prev_id=None

    def on_message(self, message):
        while True:
            colored_image_id=self._store.get('colord_id')
            gray_image_id=self._store.get('gray_id')
            if colored_image_id!=self.colored_prev_id and gray_image_id!=self.gray_prev_id :
                break
            self.colored_prev_id=colored_image_id
            self.gray_prev_id=gray_image_id
        image_colord=self._store.get('colord')
        image_gray=self._store.get('gary')
        self.write_message(tornado.escape.json_encode(dict(colored=str(image_colord).replace("b'",'').replace("'",''),gray=str(image_gray).replace("b'",'').replace("'",''))))