import cv2

cap = cv2.VideoCapture(0)

cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Live feed", cv2.flip(img, 1))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
