from user import User
from lesson import Lesson
from screen import Screen
import time, curses, sys


if len(sys.argv) > 1:
    camId = sys.argv[1]
else:
    camId = 0

# creates a new screen object
screen = Screen()
# creates a new env
les = Lesson(screen, camId)
screen.showOption()
while screen.getKey() != 113:
    screen.clear()
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
    screen.getKey()
    screen.clear()
    screen.showOption()
curses.endwin()
