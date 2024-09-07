import cv2
img=cv2.imread("car.jpg")

arabalar=cv2.CascadeClassifier("cars.xml")

gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
car=arabalar.detectMultiScale(gri,1.1,1)

for x,y,w,h in car:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("arabalar",img)
cv2.waitKey(0)
cv2.destroyAllWindows()