import cv2
img=cv2.imread("img.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.png",gray_img)
cv2.imshow("gray_img.jpg",gray_img)

