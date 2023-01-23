# # Affine Transform
# import cv2
# import numpy as np

# img = cv2.imread('image.jpg')
# row, col = img.shape[:2]

# # 변환 전, 후 좌표
# pt1 = np.float32([[200, 50], [300, 50], [200, 300]])
# pt2 = np.float32([[100, 70], [250, 70], {250, 200}])

# cv2.circle(img, (200, 50), 10, (255, 0, 0), -1)
# cv2.circle(img, (300, 50), 10, (0, 255, 0), -1)
# cv2.circle(img, (200, 300), 10, (0, 0, 255), -1)

# # Affine 변환행렬 계산 및 적용
# matrix = cv2.getAffineTransform(pt1, pt2)
# affine = cv2.warpAffine(img, matrix, (col, row))

# cv2.imshow('Origin', img)
# cv2.imshow('Affine', affine)
# cv2.waitKey()
# cv2.destroyAllWindows()

#----------------perspective Teansform--------------

# import cv2
# import numpy as np

# img = cv2.imread('/Users/doyun/ws/img/images/image.jpg')
# row, col = img.shape[:2]

# pt1 = np.float32([[0, 0], [0, row], [col, 0], [col, row]])
# pt2 = np.float32([[150, 80], [100, row - 80], [col -150, 80], [col -100, row - 80]])

# cv2.circle(img, (0, 0), 15, (255, 0, 0), -1)
# cv2.circle(img, (0, row), 15, (0, 255, 0), -1)
# cv2.circle(img, (col, 0), 15, (0, 0, 255), -1)
# cv2.circle(img, (col, row), 15, (0, 0, 0), -1)

# # 원근 변환행렬 계산 및 적용
# matrix = cv2.getPerspectiveTransform(pt1, pt2)
# perspective = cv2.warpPerspective(img, matrix, (col, row))

# cv2.imshow('Origin', img)
# cv2.imshow('Perspective', perspective)
# cv2.waitKey()
# cv2.destroyAllWindows()


#-----------------원근 변환 및 마우스 이벤트로 문서 스캔------------------
import cv2
import numpy as np

img = cv2.imread('/Users/doyun/ws/img/images/image.jpg')
draw = img.copy()

# 클릭 수 세는 변수
count = 0

#좌표 초기화
pt = np.zeros((4,2), dtype = np.float32)

def Mouse(event,x,y,flag,param):
    global count #global variance
    if event == cv2.EVENT_LBUTTONDOWN: #왼쪽 버튼 누름
        cv2.circle(draw, (x,y), 5, (0,255,0), -1)
        cv2.imshow('Scan', draw)
        pt[count] = [x,y]
        count = count + 1
        if count == 4:
                  # 좌표 상하좌우 지정
            position = pt.sum(axis = 1)
            differ = np.diff(pt, axis = 1)
            top_L = pt[np.argmin(position)] #좌측 상단
            bottom_R = pt[np.argmax(position)] #우측 하단
            top_R = pt[np.argmin(differ)] #우측 상단
            bottom_L = pt[np.argmax(differ)] #좌측 하단

            # 변환 전 좌표
            pt1 = np.float32([top_L, top_R, bottom_R, bottom_L])

            # 스캔하는 폭, 높이 계산
            width1 = abs(bottom_R[0] - bottom_L[0])
            width2 = abs(bottom_R[1] - bottom_L[1])
            height1 = abs(top_R[0] - top_L[0])
            height2 = abs(top_R[1] - top_L[1])
            width = max([width1, width2])
            height = max([height1, height2])

            # 변환 후 좌표
            pt2 = np.float32([[0,0], [width-1,0], [width-1,height-1], [0,height-1]])

            # 원근 변환
            matrix = cv2.getPerspectiveTransform(pt1, pt2)
            result = cv2.warpPerspective(img, matrix, (int(width), int(height)))
            cv2.imshow('Result', result)
cv2.imshow('Scan', img)
cv2.setMouseCallback('Scan', Mouse)
cv2.waitKey()
cv2.destroyAllWindows()