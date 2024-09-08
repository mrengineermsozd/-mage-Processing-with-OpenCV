from PIL import Image
import pytesseract

img=Image.open("adsız.PNG")
text=pytesseract.image_to_string(img,lang="eng")
print(text)