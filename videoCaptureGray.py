import cv2

capture=cv2.VideoCapture(0)
while(True):
    ret,frame=capture.read(0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('video',gray)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

