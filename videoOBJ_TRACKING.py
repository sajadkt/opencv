import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()

    new_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsvimage", new_image)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 252, 255])
    mask = cv2.inRange(new_image,lower_blue,upper_blue)
    # cv2.imshow("mask", mask)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("result",res)
    # k=cv2.waitKey(0) & 0xFF
    # if k==27:
    #     break
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()