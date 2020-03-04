import cv2, math, hough

class Keyboard:
    def __init__(self):
        self.key_positions = {
        "q":(565,295),
        "w":(505,295),
        "e":(450,295),
        "r":(390,295),
        "t":(335,295),
        "y":(280,295),
        "u":(225,295),
        "i":(170,295),
        "o":(115,295),
        "p":(65,295),
        "a":(540,265),
        "s":(480,265),
        "d":(430,265),
        "f":(375,265),
        "g":(325,265),
        "h":(270,265),
        "j":(220,265),
        "k":(165,265),
        "l":(115,265),
        "z":(502,236),
        "x":(454,236),
        "c":(400,236),
        "v":(347,236),
        "b":(297,236),
        "n":(246,236),
        "m":(198,236),
    }

        self.key_finger = {
        "q":"l0",
        "w":"l1",
        "e":"l2",
        "r":"l3",
        "t":"l3",
        "y":"r0",
        "u":"r0",
        "i":"r1",
        "o":"r2",
        "p":"r3",
        "a":"l0",
        "s":"l1",
        "d":"l2",
        "f":"l3",
        "g":"l3",
        "h":"r0",
        "j":"r0",
        "k":"r1",
        "l":"r2",
        "z":"l0",
        "x":"l1",
        "c":"l2",
        "v":"l3",
        "b":"l3",
        "n":"r0",
        "m":"r0",
    }
    def getKeyFinger(self, ltr):
    # This function is used to query the dictionary that stores which finger should be pressing which finger
    
        return self.key_finger[ltr]

    def getKeyPoint(self,ltr):
        return self.key_positions[ltr]

    def setKeyPoints(self, img):
        corners = ["q", "p", "z", "m"]
        for key in corners:
            x,y = self.key_positions[key]
            cv2.rectangle(img,(x-5,y-5),(x+5,y+5),(0,255,0),-1)

    def getCorrectFingers(self, lst_correct):
# lst correct is a list of tuples with the correct finger and the name of the image
        correct = 0
        for image in lst_correct:
            finger_choords = hough.identifyFingers(image[1])
            if self.key_finger[image[0]][0] == "l":
                if self.closest_point(image[0], finger_choords[0]):
                    correct += 1
            else:
                if self.closest_point(image[0], finger_choords[1]):
                    correct += 1
        return (correct/len(lst_correct)) * 100

         
    def closest_point(self, key, choords):
    # takes in an array of four co-ordinates and the co-ordinates of the key pressed
    # returns the index in the array which is closest to the point
        keypos = self.key_positions[key]
        i = 0
        min_dis = ""
        for c in choords:
            dist = (i, math.hypot(int(c[0]) - keypos[0], int(c[1]) - keypos[1]))
            if min_dis == "":
                min_dis = (i, math.hypot(int(c[0]) - keypos[0], int(c[1]) - keypos[1]))
            elif min_dis[1] > dist[1]:
                min_dis = dist
            i += 1
        return str(min_dis[0]) == self.key_finger[key][-1]

