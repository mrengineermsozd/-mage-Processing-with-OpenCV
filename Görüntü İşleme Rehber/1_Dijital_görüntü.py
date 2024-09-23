from pylab import  *
from PIL import Image
import cv2

img=array(Image.open("foto1.jpg").convert("L"))
print("Görüntünün dizi boyutu=",img.shape)

img1 = cv2.imread('foto1.jpg')
height, width = img.shape
print(f"Görüntü Boyutu: Yükseklik: {height}, Genişlik: {width}")