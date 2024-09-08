import cv2
import serial
import  time

arduino=serial.Serial('COM5',9600)

cap=cv2.VideoCapture(0)
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=yuz.detectMultiScale(gri,1.2,5)

    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        arduino.write(b'1')
        time.sleep(0.1)
    cv2.imshow("1",frame)
    arduino.write(b'0')

    if cv2.waitKey(50) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
