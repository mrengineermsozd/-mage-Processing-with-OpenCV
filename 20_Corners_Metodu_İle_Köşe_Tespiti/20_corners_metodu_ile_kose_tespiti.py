import cv2
import  numpy as np
img=cv2.imread("3.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray,400,0.01,10)
corners = np.int_(corners)
#noktaların bulunduğu yerlerin ağırlık merkezini bul resmin pilseline göre
for c in corners:
    x,y=c.ravel()
    cv2.circle(img,(x,y),3,(255,0,0),-1)
cv2.imshow("Ucgen",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

