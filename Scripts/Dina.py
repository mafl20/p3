import cv2


image = cv2.imread('images\\HKVM2751.JPG' , -1)
imageResized = cv2.resize(image,(500,850))
cv2.imshow("This is Frede Scoreben :D", imageResized)

cv2.waitKey(0)