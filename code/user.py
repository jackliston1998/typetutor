import operator, curses, random, sys
from keyboard import Keyboard
class User():
    def __init__(self):
    #initalises a user to store the users data
        self.score = 0
        self.miss = 0
        self.mistake = {}
        self.correct = []
    
    def setCorrect(self, letter, image_name):
    # Used to store a record of all correct key presses and their associated filenames
    # Takes in a User object, the letter pressed as a String and the name of the image as a String
    # Stores them as a tuple in the correct array which will be iterated over with our hough script to ensure correct finger used
        self.correct.append((letter, image_name))
    
    def getCorrect(self):
    # This fucntion is used to get the users correct answers
    # Takes in the User object
    # Outputs an array of tuples containing the key pressed and the name of the file that contains a screenshot the moment that key was pressed
        return self.correct
     
    def setScore(self):
    # Increments with each correct key value
    # Takes the User object    
    # Increments the User's score
        self.score += 1
    
    def getScore(self):
    # Returns the int that has been storing the amount of correct key presses made by the user
    # Takes in the User object
    # Returns the amount of correct keys pressed
        return self.score
    
    def setMiss(self):
    # Increments with each incorrect key value
    # Takes the User object    
    # Increments the User's mistakes
        self.miss += 1 
    
    def getMiss(self):
    # Returns the int that has been storing the amount of incorrect key presses made by the user
    # Takes in the User object
    # Returns the amount of incorrect keys pressed
        return self.miss
    
    def setMistake(self,ltr):
    # Adds the key that has been input incorrectly to a dictionary
    # Takes in a user object and a string representing the letter that has not been pressed correctly
    # Increments the values assigned to that key in the mistake dictionary
        if ltr in self.mistake:
            self.mistake[ltr] += 1
        else:
            self.mistake[ltr] = 1

    def getMistake(self):
    # Prints each value that was incorrect typed aswell as how many times it was incorrectly given
    # Takes in the user object
    # Outputs a list of the top three errors made, less then 3 errors it will output all errors.
        sorted_x = sorted(self.mistake.items(), key=operator.itemgetter(1))
        wrong = []
        if len(sorted_x) < 3:
            for item in sorted_x:
                # Formats the text to illustrate to the user what the value means
                wrong.append("{} wrong {} time(s)".format(item[0], item[1]))
        else:
            for i in range(3):
                # Formats the text to illustrate to the user what the value means
                wrong.append("{} wrong {} time(s)".format(sorted_x[i][0], sorted_x[i][1]))
        return wrong

    def getData(self, time, keyb):
    # Gets the data stored by the users and returns it to user
    # Takes in the user object aswell as an int refering to how long they were typing and also a keyboard object
    # Output an array containing strings for all of the user data that is return after the game
        correct_no = "{} correct key presses".format(self.getScore())
        incorrect_no =  "{} incorrect key presses".format(self.getMiss())
        wpm = "{:.2f} words per minute".format(int(((self.getScore() / time)*60)/5))
        finger_accuracy = "Finger accuracy: {:.2f}".format(keyb.getCorrectFingers(self.correct))
        if self.getScore() == 0 :
            accuracy = "accuracy = 0.00%"
        else:
            accuracy = "accuracy = {:.2f}".format(self.getScore()/(self.getMiss() + self.getScore())*100)
        return [correct_no, incorrect_no, wpm, accuracy, finger_accuracy]

if __name__ == "__main__":
    # Tests when you run python3 user.py
    user = User()
    keyb = Keyboard()
    user.setCorrect('k', 'key1.jpg')
    if user.getCorrect() == [('k', 'key1.jpg')]:
        print(True)
    user.setScore()
    if user.getScore() == 1:
        print(True)
    user.setMiss()
    if user.getMiss() == 1:
        print(True)
    user.setMistake('k')
    if user.getMistake() == ['k wrong 1 time(s)']:
        print(True)
