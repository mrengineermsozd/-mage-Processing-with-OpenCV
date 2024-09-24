import cv2
from skimage.feature import  hog
from skimage import exposure
img=cv2.imread("foto.jpg")
img=cv2.resize(img,(600,400))
gray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
_,hogimage=hog(gray,visualize=True)
rescaled=exposure.rescale_intensity(hogimage,in_range=(0,10))

cv2.imshow("HOG",hogimage)
cv2.imshow("ORJ",img)
cv2.imshow("Rescaled",rescaled)
cv2.waitKey(0)
cv2.destroyAllWindows()