from user import User
from lesson import Lesson
from keyboard import Keyboard
import time

# creates a user a/c to store the mistakes
user = User()
# creates a new env
les = Lesson()
# starts the env
les.start()
# starts a timer
start_time = time.time()
# Write words
les.writeWords(user)

# ends the timer
end_time = time.time() - start_time
# returns the user data
user.getMistake()
user.getData(end_time)

