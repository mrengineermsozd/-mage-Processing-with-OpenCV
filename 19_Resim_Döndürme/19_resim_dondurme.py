import cv2
import numpy as np
img=cv2.imread("volvo.jpg",0)
#shape bilgisine erişebilmek için resim gri tonlamalı görüntüye çevirmek gerekir.
sat,sut=img.shape
m=cv2.getRotationMatrix2D((sut/2,sat/2),90,1)
d=cv2.warpAffine(img,m,(sut,sat))
print(sat)
print(sut)
cv2.imshow("Resim",d)
cv2.waitKey(0)
cv2.destroyAllWindows()