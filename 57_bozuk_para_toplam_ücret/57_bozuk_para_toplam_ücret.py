import cv2
import  cvzone
import  requests
import numpy as np
from cvzone.ColorModule import ColorFinder
totalmoney=0
kurus5=0
kurus10=0
kurus25=0
kurus50=0
kurus1tl=0
font = cv2.FONT_HERSHEY_SIMPLEX

url="http://192.168.18.130:8080/photoaf.jpg"

img=cv2.imread("paralar.jpeg")
img1=cv2.resize(img,(600,500))

def empty(a):
    pass

#myColorFinder=ColorFinder(True)
#hsvVals = {'hmin': 10, 'smin': 55, 'vmin': 215, 'hmax': 42, 'smax': 255, 'vmax': 255}

cv2.namedWindow("Settings")
cv2.resizeWindow("Settings",640,240)
cv2.createTrackbar("Threshold1","Settings",0,255,empty)
cv2.createTrackbar("Threshold2","Settings",255,255,empty)

def onisleme(img):
    imgPre=cv2.GaussianBlur(img3,(5,3),2)
    thresh1=cv2.getTrackbarPos("Threshold1","Settings")
    thresh2 = cv2.getTrackbarPos("Threshold2", "Settings")
    imgPre=cv2.Canny(imgPre,thresh1,thresh2)
    kernel=np.ones((2,2),np.uint8)
    imgPre=cv2.dilate(imgPre,kernel,iterations=1)
    imgPre=cv2.morphologyEx(imgPre,cv2.MORPH_CLOSE,kernel)
    return imgPre


while True:
    img_resp = requests.get(url)
    arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img3 = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    img3 = cv2.resize(img3, (600, 400))
    imgPre=onisleme(img3)
    imgContours, conFound= cvzone.findContours(img3,imgPre,minArea=20)
    totalmoney=0
    kurus5=0
    kurus10 = 0
    kurus25 = 0
    kurus50 = 0
    kurus1tl = 0

    if conFound:
        for count,contour in enumerate(conFound):
            peri = cv2.arcLength(contour['cnt'], True)
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)
            if len(approx)>5:
                area=contour['area']
                #imgColor,_=myColorFinder.update(img3,hsvVals)
                print(area)
                if area<920:
                    totalmoney+=0.05
                    kurus5+=1
                elif 920<area<1100:
                    totalmoney += 0.1
                    kurus10+=1
                elif 1100<area<1300:
                    totalmoney += 0.25
                    kurus25 += 1
                elif 1300<area<1800:
                    totalmoney += 0.5
                    kurus50 += 1
                elif area>1800:
                    kurus1tl+=1
                    totalmoney += 1

    print(totalmoney)
    imgStacked = cvzone.stackImages([img3, imgPre, imgContours], 2, 0.75)
    cvzone.putTextRect(imgStacked,f'{"{:.2f}".format(totalmoney)}TL',(50,50),scale=1, thickness=1)
    cvzone.putTextRect(imgStacked, f'{kurus5} adet 5 kurus var.',(50, 100),scale=1, thickness=1)
    cvzone.putTextRect(imgStacked, f'{kurus10} adet 10 kurus var.', (50, 150), scale=1, thickness=1)
    cvzone.putTextRect(imgStacked, f'{kurus25} adet 25 kurus var.', (50, 200), scale=1, thickness=1)
    cvzone.putTextRect(imgStacked, f'{kurus50} adet 50 kurus var.', (50, 250), scale=1, thickness=1)
    cvzone.putTextRect(imgStacked, f'{kurus1tl} adet 1 tl var.', (50, 300), scale=1, thickness=1)
    cv2.imshow("Images", imgStacked)
    #cv2.imshow("ImageColor", imgColor)
    cv2.waitKey(1)
