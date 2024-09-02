import cv2
import  numpy as np
img1=cv2.imread("1.jpg")
img2=cv2.imread("2.jpg")


fark=cv2.subtract(img1,img2)
b,g,r=cv2.split(fark)
print(b)
cv2.imshow("1",fark)
"""cv2.imshow("Ucan Balon 1",res1)
cv2.imshow("Ucan Balon 2",res2)"""
cv2.waitKey(0)
cv2.destroyAllWindows()