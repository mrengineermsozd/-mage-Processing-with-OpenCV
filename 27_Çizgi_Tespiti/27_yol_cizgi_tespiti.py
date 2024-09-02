import  cv2
import numpy as np
img=cv2.imread("cizgiler.jpg")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kenar=cv2.Canny(gri,100,250)
cizgi=cv2.HoughLinesP(kenar,1,np.pi/180,75)
print(cizgi)

for i in cizgi:
    x1,y1,x2,y2=i[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imshow("Cizgi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()