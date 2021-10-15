import cv2

print("Amogus")

imageName = cv2.imread("images\\meeeee.jpg", 1)

imageResize = cv2.resize(imageName,(200,350))
cv2.imshow("Me have become resize", imageResize)
cv2.imshow("Hrello dis me", imageName)
cv2.waitKey(0)






