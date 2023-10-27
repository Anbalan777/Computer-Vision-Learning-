import cv2 
img=cv2.imread("sample2.jpg") #Read Image From Directory 
rect=cv2.rectangle(img,(10,10),(220,220),(2,255,20),5) #Draw a rectangle snytax is cv2.rectangle(src,(x,y),(x+w,x+h),(color),thickness)
cv2.putText(rect,"Python",(25,25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2) #cv2.putText(src, text, position,font,fontSize,color,thickness)
cv2.imshow("Image",img)
