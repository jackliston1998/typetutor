import operator, curses, random, sys
from keyboard import Keyboard
class User():
    #initalises a user to store the users data
    def __init__(self):
        self.score = 0
        self.miss = 0
        self.mistake = {}
        self.correct = []
        self.keyb = Keyboard()
    
    # stored tuples of the correct letter and its image name in a file to be used by OpenCV 
    def setCorrect(self, letter, image_name):
        self.correct.append((letter, image_name))
    
    #returns the list of tuples. The tuples have a the k pressed and the image at the moment it is pressed
    def getCorrect(self):
        return self.correct
     
    # increments with each correct key value
    def setScore(self):
        self.score += 1
    
    # returns the users correct key presses
    def getScore(self):
        return self.score
    
    # increments with each incorrect key value
    def setMiss(self):
        self.miss += 1 
    
    # returns the users incorrect keystrokes
    def getMiss(self):
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
                wrong.append((item[0], "wrong", item[1], "time(s)"))
        else:
            for i in range(3):
                wrong.append((sorted_x[i][0], "wrong", sorted_x[i][1], "time(s)"))
        return wrong

    # gets the data stored by the users and returns it to user
    def getData(self, time):
        accuracy = self.getScore()/(self.getMiss() + self.getScore())
        return [(self.getScore(), "correct key presses") , (self.getMiss(), "incorrect key presses"), ("accuracy = ", accuracy*100,  "%"), (int(((self.getScore() / time)*60)/5), "words per minute"), ("Finger accuracy:", self.keyb.getCorrectFingers(self.correct))]
