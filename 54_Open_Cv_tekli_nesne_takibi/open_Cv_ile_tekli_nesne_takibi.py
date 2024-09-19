import cv2

print(cv2.__version__)

trackers=["BOOSTING","MIL","CSRT","KCF","TLD","MEDIANFLOW","MOSSE"]

i=3
algoritma=trackers[i]

if algoritma=="BOOSTING":
    tracker=cv2.legacy.TrackerBOOSTING_create()
    print(tracker)
elif algoritma=="MIL":
    tracker=cv2.legacy.TrackerMIL_create()
    print(tracker)
elif algoritma=="CSRT":
    tracker=cv2.legacy.TrackerCSRT_create()
    print(tracker)
elif algoritma=="KCF":
    tracker=cv2.legacy.TrackerKCF_create()
    print(tracker)
elif algoritma=="TLD":
    tracker=cv2.legacy.TrackerTLD_create()
    print(tracker)
elif algoritma == "MEDIANFLOW":
    tracker = cv2.legacy.TrackerMEDIANFLOW_create()
    print(tracker)
elif algoritma=="MOSSE":
    tracker=cv2.legacy.TrackerMOSSE_create()
    print(tracker)

cap=cv2.VideoCapture("video.mp4")
ret,frame=cap.read()
if ret==False:
    print("Video Okunmadi")
box = cv2.selectROI(frame)
ret = tracker.init(frame, box)
print("koordinatlar", box)

while True:
    if ret == False:
        print("Video Okunmadi")
        break
    else:
        ret,box=tracker.update(frame)
        if ret==True:
            (x,y,w,h)=[int(i) for i in box]
            loc=(x,y,w,h)
            print("Konum degeri:",loc)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2,1)
            cv2.putText(frame,algoritma,(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2)
        else:
            cv2.putText(frame,"hata",(80,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2)
        cv2.imshow("pencere",frame)
        if cv2.waitKey(10) & 0xFF==ord("q"):
            break

cap.release()
cv2.destroyAllWindows()