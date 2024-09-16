import cv2
import dlib
import face_recognition
from datetime import datetime
import sqlite3

con=sqlite3.connect("yuztanima.db")
cursor=con.cursor()

def tablo():
    cursor.execute("create table if not exists kisiler(ad TEXT,zaman DATETIME)")
    con.commit()

tablo()

def ekle(isim,tarih):
    cursor.execute("Insert into kisiler Values(?,?)",(isim,tarih))
    con.commit()


detector=dlib.get_frontal_face_detector()
serhat=face_recognition.load_image_file("photo.jpg")
serhat_enc=face_recognition.face_encodings(serhat)[0]
keriman=face_recognition.load_image_file("photo2.jpg")
keriman_enc=face_recognition.face_encodings(keriman)[0]

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    face_loc=[]
    faces=detector(frame)
    for face in faces:
        x=face.left()
        y=face.top()
        w=face.right()
        h=face.bottom()
        face_loc.append((y,w,h,x))

    #face_log=face_recognition.face_locations(frame)
    face_encoding=face_recognition.face_encodings(frame,face_loc)

    i=0
    for face in face_encoding:
        y, w, h, x=face_loc[i]
        sonuc=face_recognition.compare_faces([serhat_enc],face)
        sonuc1 = face_recognition.compare_faces([keriman_enc], face)
        if sonuc[0]==True:
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"SERHAT",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
            ekle("Serhat",datetime.now())
        elif sonuc1[0]==True:
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"KERIMAN",(x,h+35),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        else:
            cv2.rectangle(frame, (x, y), (w, h), (255, 0, 0), 2)
            cv2.putText(frame, "YABANCI", (x, h + 35), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    cv2.imshow("KAMERA",frame)

    if cv2.waitKey(10) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
con.close()