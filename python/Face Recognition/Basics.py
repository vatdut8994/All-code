import cv2

img = cv2.imread("./img/known/Mommy.JPG")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (21, 21), 0)
imgCanny = cv2.Canny(img, 100, 100)


cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)


cv2.waitKey(0)
