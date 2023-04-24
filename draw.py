import cv2

image=cv2.imread("Lenna.png",1)
cv2.line(image,(0,0),(512,512),(255,0,0),5)
cv2.rectangle(image,(150,150),(362,362),(0,255,0),5)
cv2.circle(image,(50,50),50,(0,0,255),-1)
cv2.circle(image,(462,50),50,(0,0,255),-1)
cv2.circle(image,(50,462),50,(0,0,255),-1)
cv2.circle(image,(462,462),50,(0,0,255),-1)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image,"hello",(170,270),font,2,(255,255,0))

cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
