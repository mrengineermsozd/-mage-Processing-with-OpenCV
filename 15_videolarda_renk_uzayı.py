import cv2
import  numpy as np
cap=cv2.VideoCapture("video1.mp4")
while True:
    ret,frame=cap.read()
    if ret==0:
        break
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",frame)
    if cv2.waitKey(30)&0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()