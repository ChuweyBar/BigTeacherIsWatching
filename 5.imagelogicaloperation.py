import cv2
import numpy as np

c1 = cv2.imread('chuwei1.jpg')
c2 = cv2.imread('chuwei2.jpg')

# just addding pixel values together
#add = c1 + c2
#add = cv2.add(c1,c2)
#cv2.imshow('add',add)

# merge with weights
weighted = cv2.addWeighted(c1, 0.6, c2, 0.4, 0)

cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()