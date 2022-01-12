import cv2
import time

camera = cv2.VideoCapture(0)
cv2.namedWindow("Capturing your Image")

time.sleep(3)
val,window = camera.read()
if(not val):
    print("window grab faced an issue!!!")
    quit()
cv2.imshow("Capturing your Image", window)
isave = "image.png"
cv2.imwrite(isave, window)
print("{} written!".format(isave))

camera.release()
cv2.destroyAllWindows()