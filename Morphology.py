#------------침식연산---------------
import cv2
import numpy as np

img = cv2.imread('image.jpg')

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
erode = cv2.erode(img, kernel)

cv2.imshow("Erode", erode)
cv2.waitKey()
cv2.destroyAllWindows()
