from user import User
from lesson import Lesson
from screen import Screen
from camera import Camera
import time, sys, hough, os


if len(sys.argv) > 1:
    camId = int(sys.argv[1])
else:
    camId = 0
try:
    camera=Camera(camId)
    camera.showDisplay()
except:
    print("\nThere is an issue with camera with ID {}.".format(camId))
    print("Please fix the error or use a different camera.")
    sys.exit()
# creates a new screen object


screen = Screen()
# creates a new env
les = Lesson(screen, camera)
screen.showOption()
key = screen.getKey()
while key != 113:
    screen.clear()
    
    if key == 114:
        camera.showDisplay() 
        screen.scrPrint("Camera re-align fineshed", newline=True)


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
        [screen.scrPrint(n, newline=True) for n in user.getData(end_time)]
    

    elif key == 104:
        files = os.listdir()
        if len(files) == 0:
            screen.scrPrint("No images found. Complete a typing test", newline=True)
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
