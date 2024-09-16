import  cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE) #görüntüyü saat yönünde 90 derece döndürür
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE) #görüntüyü saat yönünün tersine 90 derece döndürür
    frame=cv2.rotate(frame,cv2.ROTATE_180) #görüntüyü 180 derece döndürür
    cv2.imshow("Kamera",frame)
    if cv2.waitKey(5) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()