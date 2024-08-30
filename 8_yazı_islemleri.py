import cv2
import numpy as np
canvas=np.zeros((600,600,3),np.uint8)+255
f1=cv2.FONT_ITALIC
f2=cv2.FONT_HERSHEY_DUPLEX
f3=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(canvas,"Merhaba OPENCV",(20,100),f1,2,(255,0,0),cv2.LINE_4)
cv2.putText(canvas,"Merhaba Dunya",(20,300),f2,1,(0,255,0),cv2.LINE_8)
cv2.putText(canvas,"Merhaba Yapay Zeka",(20,400),f3,1,(0,0,255),cv2.LINE_4)
cv2.imshow("Pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()