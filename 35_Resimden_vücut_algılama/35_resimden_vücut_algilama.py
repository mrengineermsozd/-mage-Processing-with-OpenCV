import cv2
img=cv2.imread("insan.jpg")
vucud=cv2.CascadeClassifier("haarcascade_fullbody.xml")
gri=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
bodies=vucud.detectMultiScale(gri,1.4,3)

for x,y,w,h in bodies:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()