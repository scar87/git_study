# #------------------평군블러링----------
# import cv2
# import numpy as np

# img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

# kernel_3 = np.ones((3,3), np.float32) / 9
# kernel_5 = np.ones((5,5), np.float32) / 25

# kernel_3_output = cv2.filter2D(img, -1, kernel_3)
# kernel_5_output = cv2.filter2D(img, -1, kernel_5)

# cv2.imshow('Img', img) #기본이미지
# cv2.imshow('kernel_3', kernel_3_output) #3*3블러링 이미지
# cv2.imshow('kernel_5', kernel_5_output) #5*5블러링 이미지

# cv2.waitKey()
# cv2.destyroyAllWindows()

#-----------------가우시안 블러링-----------
import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

#가우시안 커널 직접 생성
kernel1 = (1/16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
blur1 = cv2.filter2D(img, -1, kernel1)

#cv2.getGaussianKernel()을 통해 가우시안 커널 생성
kernel2 = cv2.getGaussianKernel(3,0)
blur2 = cv2.filter2D(img, -1, kernel2*kernel2.T)

#cv2.getGaussianKernel()를 통해 커널 생성부터 블러링까지 한 번에 처리
blur3 = cv2.GaussianBlur(img, (3,3), 0)

cv2.imshow('Image', img)
cv2.imshow('kernel1', blur1)
#blur2.blur3의 출력은 blur1 출력과 동일
#cv2.imshow('kernel2',blur2)
#cv2.imshow('kernel3',blur3)

cv2.waitKey()
cv2.destroyAllWindows()