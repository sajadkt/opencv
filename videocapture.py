import cv2
#one web cam 0
#2 web cam  use 1
capture=cv2.VideoCapture(0)

while(True):
    ret,frame=capture.read(0)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()

