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
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK) # Used for upcoming words

    # selects 30 random words and and passes them to the writeWord function
    # ends the typing enviornment 
    def start(self, user):

        # If words have not been read, then go read
        if self.words == None:
            self.getWords()
        
        # Select a number of words from the words set, no repeating wrods
        words = random.sample(self.words, 30)

        # Display message and first sets of words
        self.scrPrint("-- Type the words below. Begin by pressing \"Enter\" --", newline=True)
        self.displayWords(words[0:3], True)
        self.displayWords(words[3:6], False)
        
        # Wait til user presses enters, ord("Enters") == 10
        while self.getKey() != 10:
            pass

        # Use i instead of interating over list to chage the words
        for i in range(len(words)):

            if i < len(words) and i % 3 == 0:
                self.displayWords(words[i : i+3], True)

                if i + 2 < len(words):
                    self.displayWords(words[i+3 : i+6], False)


            written = self.writeWord(words[i], user)
            # "written" needed to know how far to go back
            self.clearLine(written)

        # Close screen when finished
        self.scrClose()


    # Get words from a list and place in a set (after striping)
    def getWords(self):
        self.words = set([word.strip() for word in open("words.txt").readlines()])


    # Display words to be typed
    # "first" is a bool to show is a line is the first or second line
    def displayWords(self, words, first):

        if first:
            self.scr.move(1, 0)
            self.scrPrint(" ".join(words), newline=True)
        
        else:
            self.scr.move(2, 0)
            self.scrPrint(" ".join(words), 3, newline=True) # 3 is to write in blue


    # Function for backspace
    def backspace(self):
        pos = curses.getsyx() # Get current cursor
        self.scr.addstr(pos[0], pos[1] - 1, " ") # Write over last character
        self.scr.move(pos[0], pos[1] - 1) # Move cursor back one


    # Fucntion for clearing a line after a word has been entered
    # "written" needed to know how far to go backwards
    def clearLine(self, written):
        pos = curses.getsyx()
        for i in range(len(written))[::-1]:
            self.scr.addstr(pos[0], i, " ")
        self.scr.move(pos[0], 0)


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


    # Fuction for testing a user on a given word
    def writeWord(self, word, user):
        # Bool list used to track if user's characters are correct
        written = []

        # Get a key press as an ASCII
        # While space is not pressed, ord(" ") == 32
        key = self.getKey()
        while key != 32:

            # Condition for backspace
            if key == 127 and len(written) > 0:
                self.backspace()  
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

        return written


    # Close the application
    def scrClose(self):
        curses.endwin()