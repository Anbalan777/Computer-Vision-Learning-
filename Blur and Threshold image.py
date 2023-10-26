import cv2
img=cv2.imread("sample2.jpg") #read image from directory with extetion 
Blur=cv2.GaussianBlur(img,(21,21),0) #Blur the image using Gaussian Blur| dst = cv2.GaussianBlur(src, (kernel),borderType)
Gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Gray image conversion 
Threshold=cv2.threshold(Gray,189,255,cv2.THRESH_BINARY)[1] #threshold image #dst = cv2.threshold(src, threshold, maxValueForThreshold,binary,type)[1] 
cv2.imshow("Normal_img",img)
cv2.imshow("Blur_Image",Blur)
cv2.imshow("grayimg",Gray)
cv2.imshow("Black&White_img",Threshold)
