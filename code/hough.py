import cv2
import sys
import numpy as np
import os

def show(image, title="Default"):
    cv2.imshow(title, image)
    key = cv2.waitKey()
    cv2.destroyWindow(title)
    return key

def detectFingers(filename, thres=180):
    img = cv2.imread(filename)
    # show(img, "original")

    copy = img.copy() # Make a copy of the image
    copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY) # Make the copy greyscale
    # show(copy, "grey")

    copy = cv2.medianBlur(copy, 15)
    # show(copy, "blur")

    # Used to see result of Canny algorithm
    # hough.Circle uses a given number as the higher threshold, and divides by 2 for the lower
    canny = cv2.Canny(copy, thres/2, thres) 
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
    circles = cv2.HoughCircles(copy, cv2.HOUGH_GRADIENT, dp=1, minDist=25, param1=thres, param2=20, minRadius=0, maxRadius=40)
    circles = np.uint16(np.around(circles))

    for (x, y, r) in circles[0, :]:
        if y >= 150:
            cv2.circle(img, (x, y), r, (0, 255, 0), 3)
        else:
            cv2.circle(img, (x, y), r, (0, 0, 255), 3)
        
        cv2.circle(img, (x, y), 2, (255, 0, 0), 2)

    # cv2.circle(img, (320, 240), 2, (255, 255, 0), 2) # center of img
    key = show(img, "{} of {}: {}".format(i, total, filename))
    return key


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
        key = detectFingers(file, 180)
        # key = lines(file)
        
        if key == 113:
            break

        i += 1