import curses
class Screen():
    def __init__(self, id=0):
        self.scr = curses.initscr()
        curses.noecho() # Stops automatic writing to the screen

        # Needed for multi-coloring
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # Used for correct text
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK) # Used for incorrect text
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK) # Used for upcoming words
    
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

    def move(self, x, y):
        self.scr.move(y, x)
