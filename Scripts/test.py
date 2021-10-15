import cv2

from TestClass import TestClass

def main_function():
    victor = TestClass()    #we make an instance of TestClass, and call it victor

    victor.martin_er_sej("amogus")  #we call the martin_er_sej()-method from the TestClass

    # > This code is run until 'return False' or a 'break'
    while True:
        user_input = cv2.waitKey(0) #we make a variable holding any user input

        image = cv2.imread('images\\linus_sad_tips.png', 0) #an image is stored

        cv2.imshow("This is sad linus", image)  #the image is shown

        if user_input == 27:    #27 is the ascii code for the <ESC> key
            break   #this breakes the while loop

    cv2.destroyAllWindows() #all windows are closed when this is reached

main_function()