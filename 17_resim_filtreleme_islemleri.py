import  cv2
import  numpy as np
img1=cv2.imread("filter.jpg")
img2=cv2.imread("median.jpg")
img3=cv2.imread("bilateral.jpg")

blr=cv2.blur(img1,(15,15))
gb=cv2.GaussianBlur(img1,(15,15),cv2.BORDER_DEFAULT)
mb=cv2.medianBlur(img2,5)
b=cv2.bilateralFilter(img3,9,75,75)
cv2.imshow("Orjinal Resim",img3)
cv2.imshow("Blurlu Resim",blr)
cv2.imshow("Gaussian Blur Resim",gb)
cv2.imshow("Median Blur Resim",mb)
cv2.imshow("Median Blur Resim",b)
cv2.waitKey(0)
cv2.destroyAllWindows()