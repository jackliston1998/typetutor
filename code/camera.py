<<<<<<< HEAD
# Uses OpenCV module and python2

=======
# OpenCV module required to run
>>>>>>> e27a56597ac7e0c7b0ec6a6cd70babf8058ec57c
import cv2
import sys # Only used for testing

# Class used to control the camera
class Camera():

    # Initailize Camera with OpenCVs Capture object
<<<<<<< HEAD
    def __init__(self):
        # VideoCapture(0) for internal cam, VideoCapture(1) for external cam
        self.capture = cv2.VideoCapture(-1)
=======
    # The id is to decide which "video" node to use, e.g "video0, video1"
    # These nodes can be found in the path "/dev"
    # Use "ls -l /dev/video*" to search all video nodes
    # Negative id will always use video0 node
    def __init__(self, id):
        self.id = id
        self.capture = cv2.VideoCapture(id)
>>>>>>> e27a56597ac7e0c7b0ec6a6cd70babf8058ec57c



    # Captures current frame, returns a tuple of length 2
    # tuple[0] is a boolean on if capture was successful
    # tuple[1] is the frame itself
    def captureFrame(self):
        return self.capture.read()



    # Shows a live capture, name is for the title of the window
    # Stop by pressing "q", this condition will change (when keyboard is detected)
    def showDisplay(self, name):
        # cv2.waitKey accepts a key press for a period of given time (in ms)
        # The key press is converted to ord, ord("q") == 113
        while cv2.waitKey(1) != 113:

            # Capture a frame, then display with imshow
            ret, frame = self.captureFrame()
            cv2.imshow(name, frame)
        
        # Remove the window when finsihed
        cv2.destroyWindow(name)



    # Used to save the current frame to a file
    # Directory determined by os, change by using os module
    def saveFrame(self, filename):
        ret, frame = self.captureFrame()
        cv2.imwrite(filename, frame)
    


    # Run when Camera is completely finished, release the Capture object
    def close(self):
        self.capture.release()


# For testing. When project finished, remove this and the "import sys" at top
if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = int(sys.argv[1])
    else:
        id = 0
    
    cam = Camera(id)
    cam.showDisplay("Keybaord")
    cam.close()

