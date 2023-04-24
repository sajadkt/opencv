import cv2
img=cv2.imread('download.jpg',0)
print(img)
cv2.imshow("image is here",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()