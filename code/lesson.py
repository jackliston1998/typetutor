import operator, curses, random, sys
from user import User
# Class to represent a lesson
class Lesson():

    # Class varible for all possible words that can be written
    # Reassign to a set of words when words are read form file once
    words = None

    # Initailize the curses application
    def __init__(self):
        self.scr = curses.initscr()
        curses.noecho() # Stops automatic writing to the screen

        # Needed for multi-coloring
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # Used for correct text
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Used for incorrect text

    # selects 10 random words and and passes them to the writeWord function
    # ends the typing enviornment 
    def start(self, user):

        if self.words == None:
            self.getWords()

        for word in range(10):
            self.writeWord(self.randInput(), user)
        self.scrClose()


    # Get words from a list and place in a set
    def getWords(self):
        self.words = set([word.strip() for word in open("words.txt").readlines()])
    

    # returns a random word from the words.txt file
    def randInput(self):
        return random.sample(self.words, 1)[0]
    

    # Function for writing to the application
    # Give a string, color and newline is optional
    def scrPrint(self, string, color=0, newline=False):
    
        if color == 0:
            self.scr.addstr(string)
        else:
            self.scr.addstr(string, curses.color_pair(color))
        
        if newline == True:
            self.scr.addstr("\n")    


    # Returns the ASCII of the a keypress
    def getKey(self):
        return self.scr.getch()


    # Close the application
    def scrClose(self):
        curses.endwin()


    # Fuction for testing a user on a given word
    def writeWord(self, word, user):
        # Bool list used to track if user's characters are correct
        written = []
        
        # Present the target word to the user
        self.scrPrint(word, newline = True)

        # Get a key press as an ASCII
        # While space is not pressed, ord(" ") == 32
        key = self.getKey()
        while key != 32:

            # Condition for backspace
            if key == 127 and len(written) > 0:
                pos = curses.getsyx() # Get current cursor
                self.scr.addstr(pos[0], pos[1] - 1, " ") # Write over last character
                self.scr.move(pos[0], pos[1] - 1) # Move cursor back one

                written = written[:-1]
            
            # Accept keys between "a" and "z"
            # Ords 97 to 122
            elif 97 <= key <= 122:
                key = chr(key) # Convert ASCII to string
            
                # Check if typed character is correct (to the given string)
                if (len(word) > len(written)) and word[len(written)] == key:
                    self.scrPrint(key, 1) # 1 is set for Green, correct text
                    user.setScore()
                    written.append(True)
                
                else:
                    self.scrPrint(key, 2) # 2 is set for Red, incorrect text
                    user.setMistake(key)
                    user.setMiss()
                    written.append(True)
            
            # Accept next keystroke before restarting loop
            key = self.getKey()
        
        # Word finished, make separation between next word
        self.scrPrint("\n\n")
