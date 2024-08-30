import cv2
import numpy as np
#img=np.zeros((20,20,3),dtype=np.uint8)+255
"""
img[0,0]=(0,0,0)
img[0,1]=(230,50,152)
img[0,2]=(140,170,180)
img[0,3]=(75,240,75)
"""
img=np.zeros((20,20),np.uint8)+255
img[0,0]=255
img[0,1]=200
img[0,2]=150
img[0,3]=100
img[0,4]=50
img[0,5]=0
img=cv2.resize(img,(500,500),interpolation=cv2.INTER_AREA)
print(img)
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()