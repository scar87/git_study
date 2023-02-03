import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

# 기분 미분 kernel 생성
G_x = np.array([[-1,1]])
G_y = np.array([[-1], [1]])

#필터적용
edge_x = cv2.filter2D(img, -1, G_x)
edge_y = cv2.filter2D(img, -1, G_y)

cv2.imshow('Edge_x', edge_x) #수평 에지
cv2.imshow('Edge_y', edge_y) #수직 에지

cv2.waitKey()


#---------------로버츠 교차필터--------------
import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

# 로버츠 교차 kenel 생성
G_x = np.array([[1,0], [0,-1]])
G_y = np.array([[0,1], [-1,0]])

# 필터 적용
edge_x = cv2.filter2D(img, -1, G_x)
edge_y = cv2.filter2D(img, -1, G_y)

cv2.imshow('Edge_x', edge_x)
cv2.imshow('edge_y', edge_y)

cv2.waitKey()
cv2.destroyAllWindows()

#-----------프리윗 필터---------
import cv2
import numpy as np

img= cv2.imread('//Users//doyun//ws//img//images//image.jpg')

# 프리윗 kernel 생성
G_x = np.array ([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
G_y = np.array ([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# 필터 적용
edge_x = cv2.filter2D(img, -1, G_x)
edge_y = cv2.filter2D(img, -1, G_y)

cv2.imshow('Edge_x', edge_x)
cv2.imshow('Edge_y', edge_y)

cv2.waitKey()
cv2.destroyAllWindows()

#-------------sobel 필터---------
#sobel 커널을 직접 생성할수도 있지만 cv2.Sobel()을 사용히면 커널을 생성하고 적용하는 것까지 한번에 수행가능
import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

#Sobel kernel 직접 생성 후 적용
G_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
G_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_x = cv2.filter2D(img, -1, G_x)
edge_y = cv2.filter2D(img, -1, G_y)

#cv2.Sobel()로 kernel 생성 및 적용
sobel_x = cv2.Sobel(img, -1, 1, 0, Ksize = 3)
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize = 3)

cv2.imshow('Edge_x', edge_x)
cv2.imshow('Edge_y', edge_y)

cv2.waitKey()
cv2.destroyAllWindows()

#--------------Scharr 필터---------------
import cv2
import numpy as np

img = cv2.imread('//Users//doyun//ws//img//images//image.jpg')

# scharr kernel 직접 생성 후 적용
G_x = np.array9([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
G_y = np.array([[-3, -10, -3], [0, 0, 0], [3, 10, 3]])

edge_x = cv2.filter2D(img, -1, G_x)
edge_y = cv2.filter2D(img, -1, G_y)

#cv2.Scharr()를 통해 kernel 생성 및 적용
scharr_x = cv2.Scharr(img, -1, 1, 0)
scharr_y = cv2.Scharr(img, -1, 0, 1)

cv2.imshow('Edge_x', edge_x)
cv2.imshow('Edge_y', edge_y)

cv2.waitKey()
cv2.destroyAllWindows()