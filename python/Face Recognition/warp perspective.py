import cv2
import numpy as np

img = cv2.imread('./img/groups/Diwali me and papa.jpg')

width, height = 1500, 750
pts1 = np.float32([[1600, 1200], [461, 619], [536, 544], [25, 25]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", imgOutput)
cv2.waitKey(0)
