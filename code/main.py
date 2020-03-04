from user import User
from lesson import Lesson
from screen import Screen
import time, curses

# creates a user a/c to store the mistakes
user = User()
# creates a new screen object
screen = Screen()
# creates a new env
les = Lesson(screen, 2)
# starts the env
les.start()
# starts a timer
start_time = time.time()
# Write words
les.writeWords(user)

# ends the timer
end_time = time.time() - start_time
# returns the user data
[print(n) for n in user.getMistake()]
[print(" ".join(map(str,n))) for n in user.getData(end_time)]

