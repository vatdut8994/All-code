import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# img[:] = 123, 255, 162
# print(img)

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 255, 255), 2)
cv2.line(img, (0, 512), (512, 0), (255, 255, 255), 2)
cv2.line(img, (256, 512), (256, 0), (255, 255, 255), 2)
cv2.line(img, (0, 256), (512, 256), (255, 255, 255), 2)
cv2.rectangle(img, (100, 100), (412, 412), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 155, (0, 0, 255), 2)
cv2.rectangle(img, (110, 110), (402, 402), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 145, (0, 0, 255), 2)
cv2.rectangle(img, (120, 120), (392, 392), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 135, (0, 0, 255), 2)
cv2.rectangle(img, (130, 130), (382, 382), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 125, (0, 0, 255), 2)
cv2.rectangle(img, (140, 140), (372, 372), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 115, (0, 0, 255), 2)
cv2.rectangle(img, (150, 150), (362, 362), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 105, (0, 0, 255), 2)
cv2.rectangle(img, (160, 160), (352, 352), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 95, (0, 0, 255), 2)
cv2.rectangle(img, (170, 170), (342, 342), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 85, (0, 0, 255), 2)
cv2.rectangle(img, (180, 180), (332, 332), (255, 0, 0), 2)
cv2.circle(img, (256, 256), 75, (0, 0, 255), 2)
cv2.rectangle(img, (190, 190), (322, 322), (255, 0, 0), 2)
cv2.putText(img, "Hello", (215, 245), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
cv2.putText(img, "World", (212, 285), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
