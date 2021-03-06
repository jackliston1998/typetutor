import random, os
# Class to represent a lesson
class Lesson():

    # Class varible for all possible words that can be written
    # Reassign to a set of words when words are read form file once
    words = None

    # Initailize the curses application and setup Camera
    def __init__(self, screen, camera):
        self.cam = camera
        self.scr = screen
        # If words have not been read, then read them
        if self.words == None:
            self.getWords()
        # If images already exits, delete all contents (last lessons photos)
        # Else, make images directory and ente
        if not os.path.isdir("images"):
            os.makedirs("images")
       
        os.chdir("images")
    
    # selects 30 random words and and passes them to the writeWord function
    # ends the typing enviornment 
    def start(self, wpl=3):
        for file in os.listdir():
            os.remove(file)
        
        # Select a number of words from the words set, no repeating wrods
        self.targetWords = random.sample(self.words, 15)

        # Display message and first sets of words
        self.scr.scrPrint("-- Type the words below, starting from the top left word --", newline=True)
        self.displayWords(self.targetWords[0:wpl], True)
        self.displayWords(self.targetWords[wpl:(2 * wpl)], False)
        self.scr.scrPrint("Press \"Space\" to begin")

        # Wait til user presses enters, ord("Enters") == 32
        while self.scr.getKey() != 32:
            pass
        
        self.scr.clearLine("Press \"Space\" to begin")

        
    def writeWords(self, user, wpl=3):
        words = self.targetWords

        # Use i instead of interating over list to change the words
        for i in range(len(words)):

            if i < len(words) and i % wpl == 0:
                self.displayWords(words[i : i+wpl], True)

                if i + 2 < len(words):
                    self.displayWords(words[i+wpl : i+(2 * wpl)], False)

            written = self.writeWord(words[i], user)
            # "written" needed to know how far to go back
            self.scr.clearLine(written)


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
            self.cam.captureFrame() # This is to clear the buffer
            ret, frame = self.cam.captureFrame()  # This frame is potentially saved

            # Condition for backspace
            if key == 127 and len(written) > 0:
                self.scr.backspace()  
                written = written[:-1]

            # Accept keys between "a" and "z" or "A" to "Z"
            elif (97 <= key <= 122) or (65 <= key <= 90):
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
