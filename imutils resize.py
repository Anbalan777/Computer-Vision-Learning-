import imutils
import cv2
img=cv2.imread("sample2.jpg")
reimg= imutils.resize(img,width=350)
cv2.imshow("Python",reimg)
