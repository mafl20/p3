import cv2

print('hello martin')

imageName = "images\\DX-9.JPG"

image = cv2.imread(imageName, -1)

cv2.imshow("MyImage",image)

cv2.waitKey(0)
cv2.destroyAllWindows()