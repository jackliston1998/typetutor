# Uses OpenCV module and python2
import cv2

# Class used to control the camera
class Camera():

    # Initailize Camera with OpenCVs Capture object
    def __init__(self):
        # VideoCapture(0) for internal cam, VideoCapture(1) for external cam
        self.capture = cv2.VideoCapture(0)



    # Captures current frame, returns a tuple of length 2
    # tuple[0] is a boolean on if capture was successful
    # tuple[1] is the frame itself
    def captureFrame(self):
        return self.capture.read()



    # Show live capture, name is for the windows title
    # Stop showing by pressing "q", stopping condition will change (when keyboard is detected)
    def showDisplay(self, name):
        # cv2.waitKey accepts a key press for a period of given time (in ms)
        # The key press is converted to ord, ord("q") == 113
        while cv2.waitKey(1) != 113:

            # Capture a frame, then display with imshow
            ret, frame = self.captureFrame()
            cv2.imshow(name, frame)
        
        # Remove window
        cv2.destroyWindow(name)



    # Used to save the current frame to a file
    # Directory determined by os, change by using os module
    def saveFrame(self, filename):
        ret, frame = self.captureFrame()
        cv2.imwrite(filename, frame)
    


    # Run when Camera is completely finished, release the Capture object
    def close(self):
        self.capture.release()



if __name__ == "__main__":
    cam = Camera()
    cam.saveFrame("frame.jpg")
    cam.showDisplay("Type Tutor")
    cam.close()

