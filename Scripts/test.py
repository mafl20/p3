import cv2

from TestClass import TestClass

def main_function():
    victor = TestClass()

    victor.martin_er_sej("amogus")

    while True:
        user_input = cv2.waitKey(0)

        image = cv2.imread('images\\linus_sad_tips.png', 0)

        cv2.imshow("This is sad linus", image)

        if user_input == 27:    #27 is the ascii code for the <ESC> key
            break

    cv2.destroyAllWindows()

main_function()