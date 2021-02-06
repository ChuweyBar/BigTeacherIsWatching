import numpy as np
import cv2

img = cv2.imread('chuwei0.jpg', cv2.IMREAD_COLOR)

# reference a pixel
px = img[55,55]

# print color of the pixel
print(px)

# change color of pixel
img[55,55] = [255,255,255]
print(px)

# region of image (subimage of image)
roi = img[20:50, 20:50]
print(roi)

# stupid way to draw square
img [100:150, 100:150] = [255,255,255]

# replace one region with another region
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()