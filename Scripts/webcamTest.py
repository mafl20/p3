import cv2

from webcam import Webcam

kamera = Webcam(cv2.VideoCapture(0))

kamera.streamWebcam()
