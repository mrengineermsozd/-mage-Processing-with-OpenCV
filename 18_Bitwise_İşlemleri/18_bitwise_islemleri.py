import cv2
import  numpy as np
img1=cv2.imread("1bit1.png")
img2=cv2.imread("2bit2.png")

bit_and=cv2.bitwise_and(img1,img2)
bit_or=cv2.bitwise_or(img1,img2)
bit_xor=cv2.bitwise_xor(img1,img2)
bit_not_img1=cv2.bitwise_not(img1)
bit_not_img2=cv2.bitwise_not(img2)
cv2.imshow("Bir",img1)
cv2.imshow("Iki",img2)
cv2.imshow("And Kapisi",bit_and)
cv2.imshow("Or Kapisi",bit_or)
cv2.imshow("Xor Kapisi",bit_xor)
cv2.imshow("Not img1",bit_not_img1)
cv2.imshow("Not img2",bit_not_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()