import operator, curses, random, sys
from keyboard import Keyboard
class User():
    def __init__(self):
    #initalises a user to store the users data
        self.score = 0
        self.miss = 0
        self.mistake = {}
        self.correct = []
        self.keyb = Keyboard()
    
    def setCorrect(self, letter, image_name):
    # Used to store a record of all correct key presses and their associated filenames
    # Takes in a User object, the letter pressed as a String and the name of the image as a String
    # Stores them as a tuple in the correct array which will be iterated over with our hough script to ensure correct finger used
        self.correct.append((letter, image_name))
    
    #returns the list of tuples. The tuples have a the k pressed and the image at the moment it is pressed
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
    # Returns
        return self.miss
    
    # adds the key that has been input incorrectly to a dictionary
    def setMistake(self,ltr):
        if ltr in self.mistake:
            self.mistake[ltr] += 1
        else:
            self.mistake[ltr] = 1

    # prints each value that was incorrect typed aswell as how many times it was incorrectly given
    def getMistake(self):
        sorted_x = sorted(self.mistake.items(), key=operator.itemgetter(1))
        wrong = []
        if len(sorted_x) < 3:
            for item in sorted_x:
                wrong.append("{} wrong {} time(s)".format(item[0], item[1]))
        else:
            for i in range(3):
                wrong.append("{} wrong {} time(s)".format(sorted_x[i][0], sorted_x[i][1]))
        return wrong

    # gets the data stored by the users and returns it to user
    def getData(self, time):
        correct_no = "{} correct key presses".format(self.getScore())
        incorrect_no =  "{} incorrect key presses".format(self.getMiss())
        wpm = "{} words per minute".format(int(((self.getScore() / time)*60)/5))
        accuracy = "accuracy = {}".format(self.getScore()/(self.getMiss() + self.getScore())*100)
        finger_accuracy = "Finger accuracy: {}".format(self.keyb.getCorrectFingers(self.correct))
        return [correct_no, incorrect_no, wpm, accuracy, finger_accuracy]






