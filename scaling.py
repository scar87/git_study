import cv2
img = cv2.imread('d:/ws/img/images/60e04a043690eb3567ad4a6e.jpg')

#LinearInterpolation
img_scale =cv2.resize(img, None, fx=1.3, fy=1.3, interpolation= cv2.INTER_LINEAR)
cv2.imshow('Linar Interpolation', img_scale)
cv2.waitKey()
cv2.destroyAllWindows

#Cubic Interpolation
img_scale = cv2.resize(img, None, fx=1.3,fy=1.3, interpolation=cv2.INTER_CUBIC)
cv2.imshow('CUBIC Interpolation', img_scale)
cv2.waitKey()
cv2.destroyAllWindows()

#Resize
img_scale = cv2.resize(img, (300,200), interpolation= cv2.INTER_AREA)
cv2.imshow('Scaling Size', img_scale)
cv2.waitKey()
cv2.destroyAllWindows