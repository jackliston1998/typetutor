import operator, curses, random, sys, os
from keyboard import Keyboard
from user import User
from camera import Camera
# Class to represent a lesson
class Lesson():

    # Class varible for all possible words that can be written
    # Reassign to a set of words when words are read form file once
    words = None

    # Initailize the curses application and setup Camera
    def __init__(self, screen, id=0):
        self.cam = Camera(id)
        self.scr = screen
    
    # selects 30 random words and and passes them to the writeWord function
    # ends the typing enviornment 
    def start(self):
        # If words have not been read, then read them
        if self.words == None:
            self.getWords()
        
        # Select a number of words from the words set, no repeating wrods
        self.targetWords = random.sample(self.words, 3)

        # If images already exits, delete all contents (last lessons photos)
        # Else, make images directory and ente
        if os.path.isdir("images"):
            os.chdir("images")
            for file in os.listdir():
                os.remove(file)
        else:
            os.makedirs("images")
            os.chdir("images")

        self.cam.showDisplay("Keyboard")

        # Display message and first sets of words
        self.scr.scrPrint("-- Type the words below. Begin by pressing \"Enter\" --", newline=True)
        self.displayWords(self.targetWords[0:3], True)
        self.displayWords(self.targetWords[3:6], False)

        # Wait til user presses enters, ord("Enters") == 10
        while self.scr.getKey() != 10:
            pass

        
    def writeWords(self, user):
        words = self.targetWords

        # Use i instead of interating over list to change the words
        for i in range(len(words)):

            if i < len(words) and i % 3 == 0:
                self.displayWords(words[i : i+3], True)

                if i + 2 < len(words):
                    self.displayWords(words[i+3 : i+6], False)

            written = self.writeWord(words[i], user)
            # "written" needed to know how far to go back
            self.scr.clearLine(written)

        # Close self.scr.when finished
        self.scrClose()


    # Get words from a list and place in a set (after striping)
    def getWords(self):
        self.words = set([word.strip() for word in open("words.txt").readlines()])


    # Display words to be typed
    # "first" is a bool to show is a line is the first or second line
    def displayWords(self, words, first):

        if first:
            self.scr.move(0, 1)
            self.scr.scrPrint(" ".join(words), newline=True)
        
        else:
            self.scr.move(0, 2)
            self.scr.scrPrint(" ".join(words), 3, newline=True) # 3 is to write in blue




    # Fuction for testing a user on a given word
    def writeWord(self, word, user):
        # Bool list used to track if user's characters are correct
        written = []

        # Get a key press as an ASCII
        # While space is not pressed, ord(" ") == 32
        key = self.scr.getKey()
        while key != 32:
            ret, buffer = self.cam.captureFrame() # This is to clear the buffer
            ret, frame = self.cam.captureFrame()  # This frame is potentially saved

            # Condition for backspace
            if key == 127 and len(written) > 0:
                self.scr.backspace()  
                written = written[:-1]

            # Accept keys between "a" and "z"
            # Ords 97 to 122
            elif 97 <= key <= 122:
                key = chr(key) # Convert ASCII to string
            
                # Check if typed character is correct (to the given string)
                if (len(word) > len(written)) and word[len(written)] == key:
                    
                    # Save an image to a file made up of the word and letter number
                    self.cam.saveFrame(frame, "{}{}.jpg".format(word, len(written) + 1))
                    user.setCorrect(key, "{}{}.jpg".format(word, len(written) + 1))
                    self.scr.scrPrint(key, 1) # 1 is set for Green, correct text
                    user.setScore()
                    written.append(True)
                
                else:
                    self.scr.scrPrint(key, 2) # 2 is set for Red, incorrect text
                    user.setMistake(key)
                    user.setMiss()
                    written.append(False)
            
            # Accept next keystroke before restarting loop
            key = self.scr.getKey()

        return written


    # Close the application
    def scrClose(self):
        curses.endwin()
