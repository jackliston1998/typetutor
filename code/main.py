from user import User
from lesson import Lesson
import time

# creates a user a/c to store the mistakes
user = User()
# creates a new env
les = Lesson()
# starts a timer
start_time = time.time()
# starts the env
les.start(user)
# ends the timer
end_time = time.time() - start_time
# returns the user data
user.getMistake()
user.getData(end_time)
