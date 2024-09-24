import cv2
import numpy as np
cap=cv2.VideoCapture(0)
def fonks(x):
    pass
cv2.namedWindow("Bar")
cv2.resizeWindow("Bar",600,600)
cv2.createTrackbar("Alt-h","Bar",0,180,fonks)
cv2.createTrackbar("Alt-s","Bar",0,255,fonks)
cv2.createTrackbar("Alt-v","Bar",0,255,fonks)
cv2.createTrackbar("Üst-h","Bar",0,180,fonks)
cv2.createTrackbar("Üst-s","Bar",0,255,fonks)
cv2.createTrackbar("Üst-v","Bar",0,255,fonks)
cv2.setTrackbarPos("Üst-h","Bar",151)
cv2.setTrackbarPos("Üst-s","Bar",255)
cv2.setTrackbarPos("Üst-v","Bar",232)
cv2.setTrackbarPos("Alt-h","Bar",0)
cv2.setTrackbarPos("Alt-s","Bar",140)
cv2.setTrackbarPos("Alt-v","Bar",146)
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    alt_h = cv2.getTrackbarPos("Alt-h", "Bar")
    alt_s = cv2.getTrackbarPos("Alt-s", "Bar")
    alt_v = cv2.getTrackbarPos("Alt-v", "Bar")
    ust_h = cv2.getTrackbarPos("Üst-h", "Bar")
    ust_s = cv2.getTrackbarPos("Üst-s", "Bar")
    ust_v = cv2.getTrackbarPos("Üst-v", "Bar")



    alt_renk=np.array([alt_h,alt_s,alt_v])
    ust_renk = np.array([ust_h, ust_s, ust_v])

    mask=cv2.inRange(frame_hsv,alt_renk,ust_renk)
    cv2.imshow("Orjinal",frame)
    cv2.imshow("Maskelenmiş", mask)
    if cv2.waitKey(20)& 0xFF==ord("q"):
        break

    if np.any(mask==255):
        print("Kirmizi Necne Algilandi")
cap.release()
cv2.destroyAllWindows()