import numpy as np
import cv2
arr = np.random.randint(0,256,(20,20), dtype=np.uint8)

#For rows
print("For rows:")
for i in range(len(arr)):
  print("Maximum of Row ", i+1,':', np.max(arr[i]))
  print("Minimum of Row ", i+1,':', np.min(arr[i]))
  print("Median of Row ", i+1,':', np.median(arr[i]))

#For Columns
print("For columns:")
arr_T = arr.T
for i in range(len(arr_T)):
  print("Maximum of Column ", i+1,':', np.max(arr_T[i]))
  print("Minimum of Column ", i+1,':', np.min(arr_T[i]))
  print("Median of Column ", i+1,':', np.median(arr_T[i]))



###Original
cv2.imshow("image", arr)
cv2.waitKey(0)
### Resizing the image and displaying
img = cv2.resize(arr, (200,200), interpolation= cv2.INTER_LINEAR)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


###Horizontal Gradient Image
l = [i for i in range(0,256)]
H_grad = list()

for i in range(0,256):
    l = [j for j in range(0,256)]
    H_grad.append(l)
H_grad = np.array(H_grad, dtype=np.uint8)

cv2.imshow("Horizontal Gradient",H_grad)
cv2.waitKey(0)
cv2.destroyAllWindows()

###Vertical Gradient
V_grad = H_grad.T
cv2.imshow("Vertical Gradient", V_grad)
cv2.waitKey(0)
cv2.destroyAllWindows()

