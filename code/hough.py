import cv2
import sys
import numpy as np
import os

def show(image, title="Default"):
    cv2.imshow(title, image)
    key = cv2.waitKey()
    cv2.destroyWindow(title)
    return key

def identifyFingers(filename):
    img = cv2.imread(filename)
    # show(img, "original")

    copy = img.copy() # Make a copy of the image
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY) # Make the copy greyscale

    copy = cv2.medianBlur(copy, 15)
    # show(copy, "blur")

    confident = detectCircles(copy)
    left = [(x, y, r) for (x, y, r) in confident if x >= 320]
    right = [(x, y, r) for (x, y, r) in confident if x < 320]
    loose = detectCircles(copy, 100, 15)
    if len(left) < 4 or len(right) < 4:
        # loose = detectCircles(copy, 100, 15)

        while len(left) < 4:
            leftX = [640, 320] + [x for (x, y, z) in left]
            leftY = [y for (x, y, r) in left]
            midX, avgY = getHueristicValues(leftX, leftY)
            left.append(min([cir for cir in loose if cir not in left], key=lambda cir: heuristic(cir, (midX, avgY))))
        
        while len(right) < 4:
            rightX = [320, 0] + [x for (x, y, z) in right]
            rightY = [y for (x, y, r) in right]
            midX, avgY = getHueristicValues(rightX, rightY)
            right.append(min([cir for cir in loose if cir not in right], key=lambda cir: heuristic(cir, (midX, avgY))))

    return sorted(left, reverse=True), sorted(right, reverse=True)

    # For testing purposes
    for (x, y, r) in loose:
        cv2.circle(img, (x, y), r, (0, 0, 255), 2)
        cv2.circle(img, (x, y), 2, (0, 0, 255), 1)

    for (x, y, r) in left:
        cv2.circle(img, (x, y), r, (255, 0, 0), 3)
        cv2.circle(img, (x, y), 2, (255, 0, 0), 2)
    
    for (x, y, r) in right:
        cv2.circle(img, (x, y), r, (255, 0, 0), 3)
        cv2.circle(img, (x, y), 2, (255, 0, 0), 2)
    
    for (x, y, r) in confident:
        cv2.circle(img, (x, y), r, (0, 255, 0), 3)
        cv2.circle(img, (x, y), 2, (0, 255, 0), 2)

    key = show(img, "{} of {}: {}".format(i, total, filename))
    return key


def detectCircles(img, edgeThres=180, circleThres=20):
    # Used to see result of Canny algorithm
    # hough.Circle uses a given number as the higher threshold, and divides by 2 for the lower
    # canny = cv2.Canny(img, edgeThres/2, edgeThres)
    # show(canny, "edge")
    
    """
    cv.Hough Circles
    Function to find circles in images. Requires 8-bit, grayscale images

    Some parameters:
    dp is the accumulator resolution ratio. Keep at 1 for co-ords to be used with original image
    minDist is the minimum distance between circles centers
    param1 is edge detection threshold. Higher value for more defined edges. See cv.Canny
    param2 is circle accumulator threshold. Lower values accept more circles
    """  
    # This should be the "conservative" search
    # minDist = 25, param1 = 180, param = 20
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=25, param1=edgeThres, param2=circleThres, minRadius=0, maxRadius=40)
    circles = np.uint16(np.around(circles)) # Round co-ords and radiuii to round numbers

    return [(x, y, z) for (x, y, z) in circles[0] if 150 <= y <= 260]


def getHueristicValues(handX, handY):
    handX = sorted(handX, reverse=True)
    spaces = [handX[i] - handX[i + 1] for i in range(len(handX) - 1)]
    biggest = max(spaces)
    pos = spaces.index(biggest)
    middleX = handX[pos] - biggest / 2

    if len(handY) == 0:
        avgY = 210
    else:
        avgY = int(sum(handY)/len(handY))

    return middleX, avgY


# Function to determine the heuristic of a circle for a given point
def heuristic(circle, point):
    (x, y, r) = circle
    (pointX , pointY) = point
    xhue = abs(pointX - x) * 10
    yhue = abs(pointY - y)
    rhue = abs(23 - r) * 3
    return xhue + yhue + rhue


if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = "images"

    os.chdir(folder)
    i = 0
    files = os.listdir()
    total = len(files)
    for file in files:
        key = identifyFingers(file)
        
        if key == 113:
            break

        i += 1
