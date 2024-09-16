import cv2
import numpy as np
import  requests

url="http://192.168.18.208:8080/photo.jpg"
#android telefondan giriş yapıp IP Webcam adlı uygulamayı indir
#ardından uygulamayı açıp en altta yer alan start server butonuna bas
#açılan pencerede alt bölümde yazan ıp adresini tarayıcıya gir 192.168.18.208:8080 bendeki adres
#açılan sekmede takephoto adlı butona bas alt bölümde yer alıyor kameranın altında
#sonra urlde yer alan kodu kopyala ve python kodunda url adresine yapıştır
while True:
    img_resp=requests.get(url)
    arr=np.array(bytearray(img_resp.content),dtype=np.uint8)
    img=cv2.imdecode(arr,cv2.IMREAD_COLOR)
    img=cv2.resize(img,(800,600))
    cv2.imshow("1",img)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()