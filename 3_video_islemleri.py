import cv2
cap=cv2.VideoCapture(0)
dosyaadi=r"C:\Users\ASUS\PycharmProjects\1_Open_CV_GİRİŞ\OPENCV\1.avi"
codec=cv2.VideoWriter_fourcc('W','M','V','2')
framerate=30
resolution=(640,480)
output=cv2.VideoWriter(dosyaadi,codec,framerate,resolution)
while True:
    ret,frame= cap.read()
    frame = cv2.flip(frame, 1)
    output.write(frame)
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1)& 0xFF==ord("q"):
        break
    cv2.waitKey(30)
cap.release()
cap.release()