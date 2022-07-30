#Importing CV2

import cv2
from cv2 import waitKey
import numpy as np
#Define the image path 

path = "D:/Diploma/wts.jpeg"

#Reading Images

img = cv2.imread(path)
#Save
#img_save = cv2.imwrite("imgnew.jpeg",img)
print(img.shape) #To show the dimentions of image


#Make width & height as vars
width, height = 400, 400


#Img resizing
img_resize = cv2.resize(img,(width, height))
print(img_resize.shape) #Toshow size of img after resizing

#To cut img
imgcrop = img[650:1280, 500:960]

imgcropresize = cv2.resize(imgcrop,(img.shape[1], img.shape[0])) #[1] is the height and [0] is the width


#TO show imgs
cv2.imshow("wts", img) 

cv2.imshow("wts Cropped", imgcrop)

cv2.imshow("wts Cropped Resized", imgcropresize)

cv2.imwrite("imgnew.jpeg",imgcrop)

cv2.imwrite("imgnew.jpeg",imgcropresize)

cv2.waitkey()






















































