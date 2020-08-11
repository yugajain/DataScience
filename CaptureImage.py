import cv2
 def take_snapshot():
     #initialising cv2
	VideoCaptureObject=cv2.VideoCapture(0)
	result=True
	while(result):
        #read the frames while the camera is on
			ret,frame=VideoCaptureObject.read()
        #cv2 .imwrite method is used to save an image to any storage device
			cv2.imwrite("np1.jpg",frame)
			result=False
        #release shuts the camera 
	VideoCaptureObject.release()
          #closes all the windows that might have opened during the proccess
	cv2.destroyAllWindows()
               #calling off function
    take_snapshot()
