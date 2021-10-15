import cv2

image = cv2.imread('images\\meeeee.jpg', -1)    #reads image from file and stores in a variable

resized_image = cv2.resize(image, (200,200))    #resizes the image and stores in a new variable

cv2.imshow("This is an image of Martin", image) #the image read is shown
cv2.imshow("Resized Martin", resized_image)     #the resized image is shown

cv2.waitKey(0)  #waits for input