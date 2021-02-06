import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("chuwei2.jpg",cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR
#IMREAD_UNCHANGED
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()