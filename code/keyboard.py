import cv2, math, hough

class Keyboard:
    def __init__(self):
        self.key_positions = {
        "q":((565,295),"l0"),
        "w":((505,295),"l1"),
        "e":((450,295),"l2"),
        "r":((390,295),"l3"),
        "t":((335,295),"l3"),
        "y":((280,295),"r0"),
        "u":((225,295),"r0"),
        "i":((170,295),"r1"),
        "o":((115,295),"r2"),
        "p":((65,295), "r3"), 
        "a":((540,265),"l0"),
        "s":((480,265),"l1"),
        "d":((430,265),"l2"),
        "f":((375,265),"l3"),
        "g":((325,265),"l3"),
        "h":((270,265),"r0"),
        "j":((220,265),"r0"),
        "k":((165,265),"r1"),
        "l":((115,265),"r2"),
        "z":((502,236),"l0"),
        "x":((454,236),"l1"),
        "c":((400,236),"l2"),
        "v":((347,236),"l3"),
        "b":((297,236),"l3"),
        "n":((246,236),"r0"),
        "m":((198,236),"r0"),
    }

    def getKeyFinger(self, ltr):
    # This function is used to query the dictionary that stores which finger should be pressing which finger
    # It takes in the target letter as a string
    # It ouput a string with the hand used and the index of the finger on that hand that should be used 
        return self.key_positions[ltr][1]

    def getKeyPoint(self,ltr):
    # This function is used to query the dictionary that stores the co-ordinates of each key.
    # It takes in a target letter as a string
    # It outputs a tuples with two ints, the x and y co-ordinates 
        return self.key_positions[ltr][0]

    def setKeyPoints(self, img):
    # This function is used to draw the four points on the initial start up frame so the user can align their keyboard
    # This takes in a numpy array that is mapped to the frame that is shown to the user
    # It will print four points onto the frame, used to align the four corners of the alpha keys on the keyboard
        corners = ["q", "p", "z", "m"]
        for key in corners:
            x,y = self.getKeyPoint(key)
            cv2.rectangle(img,(x-5,y-5),(x+5,y+5),(0,255,0),-1)

    def getCorrectFingers(self, lst_correct):
    # This function calculates what percentage of key presses used the correct finger
    # It takes an array of tuples (key pressed, image name) 
    # It ouputs the percent of amount of correct finger uses
        correct = 0
        for image in lst_correct:
            # This calls our hough transfer function which takes an image name and returns a tuple of two arrays containing the four co-ordinates each
            finger_choords = hough.identifyFingers(image[1])
            # This checks the first index frm the associated value from key_finger dic and checks which hand was used. Then it chooses the appropriate array in the tuple.
            if self.getKeyFinger(image[0])[0] == "l":
                if len(finger_choords[0]) != 4:
                    pass
                elif self.closest_point(image[0], finger_choords[0]):
                    correct += 1
            else:
                if len(finger_choords[1]) != 4:
                    pass
                elif self.closest_point(image[0], finger_choords[1]):
                    correct += 1
        if correct != 0:
            return (correct/len(lst_correct)) * 100
        else:
            return 0
         
    def closest_point(self, key, choords):
    # This function calculates which finger was used to hit the key by checking which index(i.e finger) was closest to the key that was just pressed
    # takes in an array of four co-ordinates and the co-ordinates of the key pressed
    # returns a bool on whether the closest finger is equal to the expected finger according to touch typing method.
        keypos = self.getKeyPoint(key)
        i = 0
        min_dis = ""
        # Loops through each finger and gets the distance to the target key. It stores the shortest distance in min_dis.
        for c in choords:
            dist = (i, math.hypot(int(c[0]) - keypos[0], int(c[1]) - keypos[1]))
            if min_dis == "":
                min_dis = (i, math.hypot(int(c[0]) - keypos[0], int(c[1]) - keypos[1]))
            elif min_dis[1] > dist[1]:
                min_dis = dist
            i += 1
        return str(min_dis[0]) == self.getKeyFinger(key)[-1]

if __name__ == "__main__":
    keyb = Keyboard() 
    if keyb.getKeyFinger('k') == 'r1':
        print(True)
    if keyb.getKeyPoint('k') == (165,265):
        print(True)
    print(keyb.closest_point('k',[(220,265),(165,265),(115,265),(502,236)]))
