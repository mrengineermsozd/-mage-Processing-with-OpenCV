import cv2
import numpy as np

video=cv2.VideoCapture("araclar.mp4")
backsub=cv2.createBackgroundSubtractorMOG2()
c=0



while True:
    ret,frame=video.read()
    if ret==1:
        fgmask=backsub.apply(frame)
        # Yatay çizgiler çizin
        cv2.line(frame, (0, 400), (900, 400), (255, 0, 0), 2)  # 1. yatay çizgi
        cv2.line(frame, (0, 450), (900, 450), (255, 0, 0), 2)  # 2. yatay çizgi
        countours,hiers=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try: hiers=hiers[0]
        except: hiers=[]

        for countour,hiers in zip(countours,hiers):
            (x,y,w,h)=cv2.boundingRect(countour)
            if w>40 and h>40:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                if x>50 and x<70:
                    c=c+1

        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,"ARAC:"+str(c),(90,100),font,2,(0,0,255),2,cv2.LINE_AA)

        cv2.imshow("araclar1",fgmask)
        cv2.imshow("araclar", frame)
        if cv2.waitKey(10) & 0xFF==ord("q"):
            break

video.release()
cv2.destroyAllWindows()