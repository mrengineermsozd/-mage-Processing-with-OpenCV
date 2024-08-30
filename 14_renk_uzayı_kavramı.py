"""
Renk uzayı, renklerin sayısal olarak temsil edildiği bir sistemdir ve her rengin belirli
bir koordinat veya değerler kümesiyle ifade edildiği matematiksel bir modeldir.
Renk uzayı, farklı cihazların (örneğin, monitörler, yazıcılar, kameralar) ve yazılımların
renkleri tutarlı bir şekilde işlemesine yardımcı olur.

Yaygın Renk Uzayları:
RGB (Red, Green, Blue):
Bu renk uzayı, üç temel renge dayanır: kırmızı, yeşil ve mavi. Her bir bileşen
0 ile 255 arasında bir değere sahip olabilir. Genellikle dijital ekranlarda kullanılır.

CMYK (Cyan, Magenta, Yellow, Black):
CMYK renk uzayı, dört temel renge dayanır: camgöbeği (cyan), macenta, sarı (yellow)
ve siyah. Bu model, baskı işlemlerinde yaygındır.

HSV (Hue, Saturation, Value):
Renk, doygunluk ve değer (ışıklılık) bileşenlerine dayalı bir renk uzayıdır.
Genellikle grafik ve görsel tasarımda kullanılır.

LAB (CIE Lab):*
Bu renk uzayı, insan görme sistemini modelleyen bir yapıya sahiptir ve
renklerin daha doğru bir şekilde algılanmasını sağlar. L* ışıklığı (aydınlık),
a* kırmızı-yeşil ekseni ve b* mavi-sarı eksenini ifade eder.

YUV Renk Uzayı:
Y luminance, U Chominance1, V Chominance2 kısaltmasıdır.
Y siyah, U beyaz ve V ise mavi tabanlı renklilik ve kırmızı tabanlı renkliliği
temsik eder.
"""

import cv2
import  numpy as np
img=cv2.imread("volvo.jpg")
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Resim",img)
cv2.imshow("RGB",img1)
cv2.imshow("HSV",img2)
cv2.imshow("GRAY",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
