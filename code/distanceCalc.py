import sys, math
from keyboard import Keyboard
def main(n, keyb):
    n = [n.strip() for n in open(n,"r").readlines()]
    a = []
    for elem in n:
        if elem == "":
            finger_checker(a, keyb)
            a = []
        else:
            a.append(elem)
    
    finger_checker(a, keyb)

def finger_checker(elem, keyb):
# this function takes in an array with the output data from opencv per keypress
# it assigns the target eky position to a tuple aswell as the key pressed, hand used and passes the co-ords of each finger to be parsed
# it then returns a bool of if the correct finger was used

    keypos, key, hand, coords = keyb.getKeyPoint(elem[0][-1]),elem[0][-1], hand_mirror(elem[1][0]),coords_parser(elem[2:6][::-1])
    print((hand + closest_point(coords, keypos)) == keyb.getKeyFinger(key))
    
def hand_mirror(hand):
# reverses the hand as opencv is looking at the hand inverted
    if hand == "r":
        return "l"
    else:
        return "r"


def closest_point(coords, key):
# takes in an array of four co-ordinates and the co-ordinates of the key pressed
# returns the index in the array which is closest to the point
    i = 0
    min_dis = ""
    for c in coords:
        dist = (i, math.hypot(int(c[0]) - key[0], int(c[1]) - key[1]))
        if min_dis == "":
            min_dis = (i, math.hypot(int(c[0]) - key[0], int(c[1]) - key[1]))
        elif min_dis[1] > dist[1]:
            min_dis = dist
        i += 1
    return str(min_dis[0])


def coords_parser(coords):
# this parses the output from opencv and returns an array of four co-ordinates
    n = [(n.split("[")[1]).split(" ") for n in coords] 
    a = []
    for coords in n:
        if coords[0] == "":
            a.append((coords[1],coords[2]))
        else:
            a.append((coords[0],coords[1]))
    return a
if __name__ == "__main__":
    keyb = Keyboard()
    main(sys.argv[1],keyb)
