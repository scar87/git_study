import cv2

#LinearInterpolation
img_scale =cv2.resize(img, None, fx=1.3, fy=1.3, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Liner Interpolation', img_scale)
cv2.waitKey()
cv2.destroyAllWindows