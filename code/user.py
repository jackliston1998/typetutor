import operator, curses, random, sys
class User():
    #initalises a user to store the users data
    def __init__(self):
        self.score = 0
        self.miss = 0
        self.mistake = {}
        self.correct = []
    
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
        for item in sorted_x:
            print(item[0], "wrong", item[1], "time(s)")
    
    # gets the data stored by the users and returns it to user
    def getData(self, time):
        accuracy = self.getScore()/(self.getMiss() + self.getScore())
        print(self.getScore(), "correct key presses") 
        print(self.getMiss(), "incorrect key presses")
        print("accuracy = ", accuracy*100,  "%")
        print(int(((self.getScore() / time)*60)/5), "words per minute")
        print(self.correct)
