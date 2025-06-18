import cv2
import numpy as np

img = cv2.imread('D:\Bull.jpg')

cv2.imshow("Original", img)
cv2.waitKey(0)
###Grayscale and apply Gaussian Blur
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Grayscale
img_gray_blur = cv2.GaussianBlur(img_gray, ksize=(9,9), sigmaX=100)
cv2.imshow("Gray and Gaussian Blur", img_gray_blur)
cv2.waitKey(0)


l = list()
for i in range(img.shape[0]):
    l1 = list()
    for j in range(img.shape[1]):
        l1.append(255)
    l.append(l1)
white_img = np.array(l, dtype= np.uint8)
white_img_2 = np.ones(shape=(466,474), dtype=np.uint8)*255 #A better way
img_gray_blur_inv = white_img_2 - img_gray_blur
cv2.imshow("Inverted", img_gray_blur_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

###Question 3
blank_img = np.zeros(shape=(512,512,3), dtype=np.uint8)


cv2.rectangle(blank_img, (50,50), (462,462), (255,0,0), 3)
cv2.imshow('Draw', blank_img)
cv2.circle(blank_img,(300,300), 50, (0,255,0))
cv2.line(blank_img, (50,50), (462,462), (0,0,255), 2)
cv2.imshow('Draw', blank_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
