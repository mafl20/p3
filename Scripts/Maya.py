import cv2

image = cv2.imread ("images\\meeeee.jpg", 1)

resizeimage=cv2.resize(image, (200,200))

cv2.imshow("Hej",image)

cv2.waitKey(0)

