import cv2

cap=cv2.VideoCapture("cars.mp4")
araba=cv2.CascadeClassifier("cars.xml")

while True:
    ret,frame=cap.read()
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=araba.detectMultiScale(gri,1.1,2)

    for x,y,w,h in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("Arabalar",frame)
    if cv2.waitKey(20) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()