import cv2
import numpy as np

img = cv2.imread('D:\Bull.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Original", img)
cv2.waitKey(0)

###inversion
img_inv = 255 - img
cv2.imshow("Inverted", img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()


###RGB without red

img = cv2.imread('D:\Bull.jpg',cv2.IMREAD_COLOR)
###Manual Way

m , n, c = img.shape
for i in range(m):
    for j in range(n):
        img[i][j][2] = 0
cv2.imshow("Red zeroed Out", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow("Red out", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('D:\Bull.jpg',cv2.IMREAD_COLOR)

flip_hori = cv2.flip(img, 1)
flip_vert = cv2.flip(img, 0)
flip_mirror = cv2.flip(img, 1)
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.imshow("Vertical", flip_vert)
cv2.waitKey(0)
cv2.imshow("Horizontal", flip_hori)
cv2.waitKey(0)
cv2.imshow("Mirror", flip_mirror)
cv2.waitKey(0)
cv2.destroyAllWindows()
