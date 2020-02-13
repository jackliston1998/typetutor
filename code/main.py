from user import User
from lesson import Lesson

# creates a user a/c to store the mistakes
user = User()
# creates a new env
les = Lesson()
# starts the env
les.start(user)
# returns the user data
user.getMistake()

