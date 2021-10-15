import cv2

image = cv2.imread('images\\FridayNight.png', -1)

imageResized = cv2.resize(image, (800, 450))

cv2.imshow("This is an image embodying chaos", imageResized)

cv2.waitKey(0)