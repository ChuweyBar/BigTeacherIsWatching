import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("chuwei2.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR
#IMREAD_UNCHANGED
#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
"""
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth='5')
plt.show()


#cv2.imwrite("graychuwei.png",img)
# capture video from webcam
cap = cv2.VideoCapture(1)
# how to output video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
"""

img = cv2.imread('chuwei2.jpg', cv2.IMREAD_COLOR)

# draw line
cv2.line(img, (0,0), (150,150), (255,255,255),15)
# draw rectangle
cv2.rectangle(img, (15,25), (200,150), (0,255,0),5)
# draw circle
cv2.circle(img, (100,75), 55, (0,0,255), -1)
# draw polygons
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
# True means we want to connect last point to first line
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Big Teach', (0,130), font, 1, (255,255,0), 2 , cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()