import cv2

img = cv2.imread('./img/known/Me.jpg')
print(img.shape)

imgCropped = img[350:3000, 850:2600]
print(imgCropped.shape)

imgResize = cv2.resize(imgCropped, (200, 300))
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
