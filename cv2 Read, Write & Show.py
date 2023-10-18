import cv2 #import the opencv lib
img=cv2.imread("sample2.jpg") #ready image from directory 
cv2.imshow("Python",img) #display the image 
cv2.imwrite("Pytohn.jpg",img) #Save the image
cv2.waitKey() # time 
cv2.destroyAllWindows() colse the window an particular time

