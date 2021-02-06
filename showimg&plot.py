import cv2
import numpy as np
import matplotlib.pyplot as plt

# Tells OpenCV which image to read
# GRAYSCALE turn it gray
img = cv2.imread('chuwei0.jpg', 0)

# Other options
# IMREAD_COLOR = 1(color) = 0 grayscale
# IMREAD_UNCHANGED = -1

"""
# show the image
cv2.imshow('image',img)
# trigger when any key is pressed
cv2.waitKey(0)
# kill all windows
cv2.destroyAllWindows()
"""
# show img with matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
# how to plot line (start, finish, color, width)
plt.plot([50,100],[80,100], 'c', 5)

# how to save img
cv2.imwrite('graychuwei.png', img)

# show the matplotlib
#plt.show()
