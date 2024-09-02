import cv2
cap=cv2.VideoCapture("insanlar1.mp4")
# İstediğin yeni boyutları belirle
scale_percent = 50  # Orijinal boyutun yüzde kaçı olacak
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) * scale_percent / 100)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) * scale_percent / 100)
dim = (width, height)
yuz=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
    ret,resized_frame=cap.read()
    resized_frame = cv2.resize(resized_frame, dim, interpolation=cv2.INTER_AREA)
    gri=cv2.cvtColor(resized_frame,cv2.COLOR_BGR2GRAY)
    faces=yuz.detectMultiScale(gri,1.2,5)

    for x,y,w,h in faces:
        cv2.rectangle(resized_frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow("Resim",resized_frame)
    if ret==0:
        break
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

