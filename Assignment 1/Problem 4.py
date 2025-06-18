import cv2
import numpy as np
img = cv2.imread('D:\Bull.jpg')


###Size and Pixel values
print("Size:",np.size(img))
print("Shape:", img.shape)
print("Red:", img[:,:,2])
print("Green:", img[:,:,1])
print("Blue:", img[:,:,0])


def cvt_cg(img):
    R = img[:,:,2]
    G = img[:,:,1]
    B = img[:,:,0]
    arr = ((0.299*R)+(0.587*G)+(0.114*B))
    arr = np.array(arr, dtype=np.uint8)
    return arr
arr_gray = cvt_cg(img)
cv2.imshow("Gray",arr_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

###Count number of white
count = 0
white = [255,255,255]
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if list(img[i][j])==white:
            count+=1
print(count)