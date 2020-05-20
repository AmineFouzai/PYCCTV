# PYCCTV
Webcam over WebSocket using OpenCV and Tornado With Nigth Vison Mode(grayscale) and Light Mode And Face Reacognation
<hr>
<h1>#setup:</h1>
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
<hr>
<h1>#Theory:</h1>
<h4>-the purpose of this project is to mimic a cctv over network using websocket protocol with web technologies. <h4>
<h4>-A CCTV  pick up the images, which are then transmitted then to a recording device and then a monitor in this case the webcam well save the images with the help of opencv then saving it to redis and send it via tornado server to a real time show on te browser. </h4>
<h4>#this kind of way called a MJPEG Stream</h4>
<h1>#Technologies:</h1>
<h3>Redis:</h3>
<img src="">
<h4>Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broke</h4>
<br>
<h3>OpenCV:</h3>
  <img src="">
<h4>OpenCV is a library of programming functions mainly aimed at real-time computer vision and highly optimized .</h4>
<br>
  <h1>#Resualt:</h1>
 <h3>Motion MJPEG</h3>
  <h4>In multimedia, Motion JPEG (M-JPEG or MJPEG) is a video compression format in which each video frame or interlaced field of a digital video sequence is compressed separately as a JPEG image</h4>
  <img src="">
  <br>
  <hr>
  <h2>#For Future Usage:</h2>
  <h4>-the "video" is streamd via a html "img" tag ☺ it would be grate if i cant do the same with audio .</h4>
