import cv2
img=cv2.imread("Image Location with Extention")
gray img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.png",gray img)
cv2.imshow(gray img)

