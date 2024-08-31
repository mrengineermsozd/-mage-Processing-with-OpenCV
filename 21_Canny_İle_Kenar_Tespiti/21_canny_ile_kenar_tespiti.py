import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    kenar=cv2.Canny(frame,100,200)
    cv2.imshow("Orjinal",frame)
    cv2.imshow("Canny",kenar)
    if cv2.waitKey(10) & 0XFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()