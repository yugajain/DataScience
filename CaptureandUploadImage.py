
import cv2
import dropbox
import time
import random


start_time=time.time()
 def take_snapshot():
     number=random.randint(0,100)
     VideoCaptureObject=cv2.VideoCapture(0)
      
	 result=True
     while(result):
        #read the frames while the camera is on
			ret,frame=VideoCaptureObject.read()
            img_name="image"+str(number)+".png"
        #cv2 .imwrite method is used to save an image to any storage device
			cv2.imwrite(img_name,frame)
            start_time=time.time()

			result=False
    return img_name
    print("snapshots taken")
        #release shuts the camera 
	 VideoCaptureObject.release()
          #closes all the windows that might have opened during the proccess

	 cv2.destroyAllWindows()
def upload_file(img_name):
    access_token=""
    file = image_counter
    file_from = file
    file_to = "/new folder 1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
   with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
