import cv2
import numpy as np
#görüntü birleştirme için boyutların aynı olması gerekmektedir. Matrislerde toplama yapacağımız için
daire=np.zeros((512,512,3),np.uint8)+255
cv2.circle(daire,(256,256),50,(255,0,0),-1)
kare=np.zeros((512,512,3),np.uint8)+255
cv2.rectangle(kare,(150,150),(350,350),(0,255,0),-1)
topla=cv2.add(daire,kare)
print(topla[256,256])
cv2.imshow("Daire",daire)
cv2.imshow("Kare",kare)
cv2.imshow("Topla",topla)
cv2.waitKey(0)
cv2.destroyAllWindows()