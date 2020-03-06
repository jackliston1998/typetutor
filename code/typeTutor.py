from user import User
from lesson import Lesson
from screen import Screen
from camera import Camera
from keyboard import Keyboard
import time, sys, hough, os

# Initializing the keyboard
keyb = Keyboard()

# Allowing the user to choose a video node if more than one is available
if len(sys.argv) > 1:
    camId = int(sys.argv[1])
else:
# If no node is specified then 0 will be set as the default node
    camId = 0
try:
# If the user has no camera, unplugs camera or incorrectly configures camera it will exit the environment and give feedback to the user.
    camera=Camera(camId)
    camera.showDisplay(keyb)
except:
    print("\nThere is an issue with camera with ID {}.".format(camId))
    print("Please fix the error or use a different camera.")
    sys.exit()
# Creates a new screen object
screen = Screen()
# Creates a new lesson object
les = Lesson(screen, camera)
# This prints the menu to the user upon starting the game up
screen.showOption()
# This captures the users input key to determine which mode they requested
key = screen.getKey()
while key != 113:
    # This clears the screen at as the user's request for the mode is no process
    screen.clear()
    # If the user presses the 'r' key then they will open a live display with the alignment tool.
    if key == 114:
        camera.showDisplay(keyb) 
        screen.scrPrint("Camera re-align finished", newline=True)
        screen.continuePrompt()
    # If the user presses the 'p' key then the game will be started
    elif key == 112:
        # starts the env
        les.start()
        # creates a user a/c to store the mistakes
        user = User()
        # starts a timer
        start_time = time.time()
        # Write words
        les.writeWords(user)
        # ends the timer
        end_time = time.time() - start_time
        screen.clear()

        # returns the user data
        [screen.scrPrint(n, newline=True) for n in user.getMistake()]
        [screen.scrPrint(n, newline=True) for n in user.getData(end_time, keyb)]
        
        # The prompt does no appear until the user sees there data so they don't accidentally skip the data while it is loading
        screen.scrPrint("Press 'c' to continue")
        while screen.getKey() != 99:
            pass
                 
    # If the user presses the 'h' key then the demo mode will be entered in which the user steps through all the images from ther last game and can see the hough circles that we calculated on each image.
    elif key == 104:
        files = os.listdir()
        # if their are no saved images then informs the user
        if len(files) == 0:
            screen.scrPrint("No images found. Complete a typing test", newline=True)
        # otherwise it displays the instructions to the user and cycles through the images and displays them with the hough circles overlayed
        else:
            screen.scrPrint("When in OpenCV screen, press any key to see the next image.\nPress q to quit.\n\nPress any key to open OpenCV screen\n")
            screen.getKey()
            for filename in sorted(files):
                img = hough.identifyFingers(filename, testing=True)
                key = hough.show(img, filename) 
                
                if key == 113:
                    break

            screen.clear()
            screen.scrPrint("Hough demo finished", newline=True)

        screen.continuePrompt()
    screen.clear()
    screen.showOption()
    key = screen.getKey()

screen.closeScreen()
