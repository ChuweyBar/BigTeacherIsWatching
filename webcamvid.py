import cv2
import numpy as np

# 0 is default but 1 catches logitech capture
cap = cv2.VideoCapture(1)
# saving video to local
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.Videowriter('output.avi', fourcc, 20.0, (640,480))

while True:
    # ret is true / false, if feed then see video if not then boom
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    # if q is pressed end video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()