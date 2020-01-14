import numpy as numpy
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture each frames
    ret, frame = cap.read()

    #display resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()