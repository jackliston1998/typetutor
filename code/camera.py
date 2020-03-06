# OpenCV module required to run
import cv2
import sys # Only used for testing
from keyboard import Keyboard

# Class used to control the camera
class Camera():

    # Initailize Camera with OpenCVs Capture object
    # The id is to decide which "video" node to use, e.g "video0, video1"
    # These nodes can be found in the path "/dev" for linux
    # Use "ls -l /dev/video*" to search all video nodes
    # Negative id will always use video0 node
    def __init__(self, id=0):
        self.id = id
        self.capture = cv2.VideoCapture(id)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1) # Change buffer size to one photo

    def captureFrame(self):
    # Captures current frame, returns a tuple of length 2
    # Takes in a camera object
    # Returns a tuple of tuple[0] is a boolean on if capture was successful and tuple[1] is the frame itself(numpy array)
        return self.capture.read()


    def saveFrame(self, frame, filename):
    # Used to save the a frame, directory determined by os, change by using os module
    # Takes in a camera object, the frame(numpy array) and a string that is the name that the file will be called
        # ret, frame = self.captureFrame()
        cv2.imwrite(filename, frame) 

    def showFrame(self, frame, name="Camera"):
    # Used to dispaly a frame to the screen
    # Takes in the camera object, the frame you would like to be show aswell as the name you would like to show on the border of the image display 
    # Used to dispaly a frame to the screen
        cv2.imshow(name, frame)


    def showDisplay(self, keyb):
    # Shows a live capture, name is for the title of the window
    # Takes in the camera object aswell as a keyboard object so the alignment aid can be output
    # A live feed of the webcam with the alignment aid overlayed
        # cv2.waitKey accepts a key press for a period of given time (in ms)
        # The key press is converted to ord, ord("q") == 113
        while cv2.waitKey(1) != 113:

            # Capture a frame, then display with imshow
            ret, frame = self.captureFrame()
            keyb.setKeyPoints(frame)
            self.showFrame(frame, "Align Keyboard - Press \"q\" to quit")
        
        # Remove the window when finsihed
        cv2.destroyWindow("Align Keyboard - Press \"q\" to quit")


    # Run when Camera is completely finished, release the Capture object
    def close(self):
        self.capture.release()


# For testing. When project finished, remove this and the "import sys" at top
if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 0
    keyb = Keyboard()
    cam = Camera(id)
    cam.showDisplay(keyb)
    cam.close()

