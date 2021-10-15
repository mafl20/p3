import cv2  #opencv is imported

class Webcam:   #class definition is begun
    webCam = None;  #a variable that stores nothing, for now

    # > contructor 
    def __init__(self, webCam): #> init = initialization
        self.webCam = webCam
        
    # > method
    def streamWebcam(self):
        # Check if the webcam is opened correctly
        if self.webCam.isOpened() == False:
            raise IOError("Cannot open webcam")

        while True:

            ret, frame = self.webCam.read() #camera is read and stored in 'frame'
            cv2.imshow('Input', frame)  #frame is shown

            user_input = cv2.waitKey(1) #wait for user input
            if user_input == 27: #ascii code for <ESC> key
                break

        self.webCam.release()
        cv2.destroyAllWindows() # closes all windows