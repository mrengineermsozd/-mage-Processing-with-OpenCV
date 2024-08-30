import cv2
img=cv2.imread("301808.jpg")
roi=img[220:275,120:220]
cv2.imshow("Resim",img)
cv2.imshow("roi",roi)
#roi kullanılarak görüntü üzerinde küçültme işlemi uygulanır bu sayede algoritmalar daha hızlı çalışabilir
cv2.waitKey(0)
cv2.destroyAllWindows()