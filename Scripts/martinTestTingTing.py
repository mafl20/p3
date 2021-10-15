import cv2

print("Amogus")

imageName = "images\\meeeee.jpg"

image = cv2.imread(imageName, -1)

cv2.imshow("MyImage",image)

cv2.waitKey(0)
cv2.destroyAllWindows()