import cv2


face_cascade = cv2.CascadeClassifier('cascade_frontface_default.xml')

img = cv2.imread('bill.png')
print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_img)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=4)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()