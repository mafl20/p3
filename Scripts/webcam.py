import cv2

class Webcam:
    webCam = None;

    def __init__(self, webCam):
        self.webCam = webCam
        
    def streamWebcam(self):
        # Check if the webcam is opened correctly
        if self.webCam.isOpened() == False:
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = self.webCam.read()
            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break

        self.webCam.release()
        cv2.destroyAllWindows()
        
