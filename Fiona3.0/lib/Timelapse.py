import time
import picamera
import os

FRAMES_PER_HOUR = 360
FRAMES = FRAMES_PER_HOUR * 24

def capture_frame(frame):
	with picamera.PiCamera() as cam:
        cam.resolution = (2592, 1944)
		time.sleep(2)
		cam.capture("/resources/images/frame%03d.jpg" % frame)

for frame in range(FRAMES):
	start = time.time()
	
	capture_frame(frame)
	time.sleep(int(60*60 / FRAMES_PER_HOUR) - (time.time() - start))

os.system("ffmpeg -r 10 -i /resources/images/frame%03d.jpg -c:v libx264 video-file.mp4import time")
