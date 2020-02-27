import numpy as np
import cv2, sys

# Load an color image in grayscale
img = cv2.imread(sys.argv[1],1)

key_positions = {
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
for key in key_positions:
    x,y = key_positions[key]
    cv2.rectangle(img,(x-5,y-5),(x+5,y+5),(0,255,0),-1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
