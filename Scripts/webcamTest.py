import cv2  #opencv is imported

from Classes.webcam import Webcam   #the Webcam-class is imported from webcam.py

kamera = Webcam(cv2.VideoCapture(0))    #instance of WebCam-class, with the primary camera of the device passed in

kamera.streamWebcam()   #the method stated in the class is called