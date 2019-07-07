import cv2
import numpy as np
import os

# Playing video from file:
nameOfVideo = 'name.mp4'
cap = cv2.VideoCapture(nameOfVideo)
from moviepy.editor import VideoFileClip
clip = VideoFileClip(nameOfVideo)
print( clip.duration )

bb = clip.duration*30
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

    # Just for security purposes
    if currentFrame > bb:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
