import numpy as np
import cv2, sys

# Load an color image in grayscale
img = cv2.imread(sys.argv[1],1)

key_positions = {
    "q":(585,250),
    "w":(525,250),
    "e":(465,250),
    "r":(405,250),
    "t":(345,250),
    "y":(295,250),
    "u":(245,250),
    "i":(185,250),
    "o":(125,250),
    "p":(65,250),
    "a":(560,225),
    "s":(500,225),
    "d":(447,225),
    "f":(394,225),
    "g":(340,225),
    "h":(286,225),
    "j":(232,225),
    "k":(179,225),
    "l":(123,225),
    "z":(526,206),
    "x":(466,206),
    "c":(414,206),
    "v":(363,206),
    "b":(315,206),
    "n":(260,206),
    "m":(210,206),
}
for key in key_positions:
    x,y = key_positions[key]
    cv2.rectangle(img,(x-5,y-5),(x+5,y+5),(0,255,0),-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
