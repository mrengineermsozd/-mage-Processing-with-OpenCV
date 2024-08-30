import cv2
import numpy as np
img=cv2.imread("301808.jpg")
img[200,300,0]=0
print(img[200,300])
mavi=img.item(150,150,0)
print(mavi)
#img.itemset((150,150,0),200)
print(img[150,150])
"""renk=img[200,200]
print("Renkler:" ,renk)
mavi=img[200,200,0]
print("Mavi:",mavi)
yesil=img[200,200,1]
print("Yeşil:",yesil)
kirmizi=img[200,200,2]
print("Kırmızı:",kirmizi)
#print(img.shape)"""
cv2.imshow("araba",img)
cv2.waitKey(0)
cv2.destroyAllWindows()