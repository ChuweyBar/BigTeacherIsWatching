import cv2
import numpy as np

img = cv2.imread('book.JPG')

# anything above 12 is white else its black
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

#grayscale it then do above
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
# adaptive threshold
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('gauss',gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()