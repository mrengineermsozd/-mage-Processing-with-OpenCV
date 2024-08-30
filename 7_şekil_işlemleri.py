import cv2
import  numpy as np
canvas=np.zeros((500,500,3),np.uint8)+255
#cv2.line(canvas,(100,100),(300,300),(0,255,255),thickness=5)
#cv2.line(canvas,(200,200),(330,400),(0,255,0),8)
cv2.rectangle(canvas,(30,30),(60,60),(0,255,0),6)
cv2.circle(canvas,(100,100),50,(255,0,0),6)
u1=(250,250)
u2=(250,350)
u3=(300,350)
cv2.line(canvas,u1,u2,(75,255,89),thickness=5)
cv2.line(canvas,u2,u3,(90,150,150),thickness=5)
cv2.line(canvas,u1,u3,(175,65,180),thickness=5)

cv2.imshow("Pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()