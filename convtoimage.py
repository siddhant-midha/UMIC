# Importing all necessary libraries
import cv2
import os
  
# Read the video from specified path
cam = cv2.VideoCapture("initial_mast_training_001.mp4")
  
try:
      
    # creating a folder named data
    if not os.path.exists('initial_mast_training_001'):
        os.makedirs('initial_mast_training_001')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
  
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:

	   # if video is still left continue creating images
           name = './initial_mast_training_001/%06d.jpg'%(currentframe)
           print ('Creating...' + name)
	  
		# writing the extracted images
           cv2.imwrite(name, frame)
	  
		# increasing counter so that it will
		# show how many frames are created
    currentframe += 1

    if not ret:
        break
  
# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
