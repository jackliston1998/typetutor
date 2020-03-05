# Type Tutor: User Manual

This manual will show how to use the Type Tutor program. Our program will use a camera to monitor your fingers as you type one of our lesson. Afterwards, you will be given feedback on your lesson and can you review the images to better understand how you are typing and where you can improve.


### Requirements
There are some requirements to be able run the program correctly.

__Hardware requirements:__
- QWERTY, English keyboard
    - Your keyboard must have the standard "QWERTY" layout for the 26 letters of the English alphabet. 
- Suitable camera
    - The chosen camera must be able to focus on the keyboard. An in-built laptop camera can not be used on the same laptops keyboard.
- Moderate sized desk
    - Some space is required to set up the camera and the keyboard properly.

__Software requirements:__
- Linux machine
    - Computer must be running a version of Linux.
- Python3
    - Programming language, preferably the latest update.
- OpenCV library (python3 version)
    - This library is used for image recognition and image capturing. It is used to capture images during the lesson and the analysis afterwards


### Installation and Running
There is no installation required apart from downloading the correct folder. However, you will need to prepare your keyboard and camera before beginning. Make sure they are both working with your computer

Once downloaded, Open your terminal and find the folder. Find the python file "typeTutor.py" and run it from your terminal. 

![](https://i.imgur.com/bBbGWID.png)

You can also type a number beside the file name to switch which camera is being used. This number represents the *ID* of a camera and determines which camera to use. If no number is passed, the ID defaults to 0. To check all available cameras, use *"ls /dev/video\*"* to list all the connected camera devices with their IDs.

![](https://i.imgur.com/rpYbW51.png)


### Camera Setup
After running the file, the first thing to do is setup your camera to monitor the keyboard. 

1. If the camera is working, a live feed from the camera should appear on screen. On this feed, there will be 4 green *"alignment"* dots.
2. Begin by placing your keyboard in a comfortable position for typing.
3. Move the camera so that the alignment dots are on the four corner letters (top pair of dots on "m" and "z", bottom pair on "p" and "q"). See the images below for reference.
4. When the camera has been successfully aligned, press "q" to quit out of the alignment window.

![](https://i.imgur.com/BKLYMCe.png)

![](https://i.imgur.com/1ouavE6.png)

*Recommendation:* Try to move the camera to align with the keyboard, rather than moving the keyboard. You may move the keyboard into an uncomfortable position for typing.


### Menu

![](https://i.imgur.com/9rlkxT2.png)

After the alignment, you will see a menu with 4 different options:
- Play the game ("p")
    - Start a brand new typing lesson
- Demo hough ("h")
    - This option shows you the images from your most recent typing lesson. It will also show you how the program attempts to identify your fingers
- Re-align camera ("r")
    - If the camera and keyboard are no longer in line, this option will allow you to re-set the camera, similar to the start of the lesson.
- Quit the program ("q")
    - Exit the Type Tutor program


### Taking a lesson

The first few words to type will be displayed on screen in white and blue. The white line is the words you are currently typing and the blue line is upcoming words. You begin by typing the white words, starting from the left. When you have finished the white line, the blue line will move up and become the white line, the next set of words to type. New words will populate the blue line. This will continue until the end of the lesson

![](https://i.imgur.com/pCD8Ukb.png)

The program will wait for you to first enter space before beginning. When you are typing out the words, your letters will appear in different colours depending on whether they are right or wrong. If the right letter is typed, the letter will appear in green. If the wrong letter is typed, it will appear in red. This is to help you recognize your mistakes.

![](https://i.imgur.com/95LoJ7v.png)

At the end of the lesson, your results will be returned. These include mistakes made, speed and your finger accuracy.


### Finger detection demo

When you complete a lesson, the program takes the images and tries to detect your finger tips to determine if you are correctly touch typing. This option allows you to check the finger detection for the last completed lesson.

The program will cycle through the images, showing them to you one at a time. Included in the image will be different coloured circles. These circles represent how the program is detecting your fingers. You can press any key to continue onto the next image and press "q" to quit.

![](https://i.imgur.com/QIFfFgt.png)

__Circle colour key:__
- Green circles represent what the program is confident is a circle
- Red circles are potential fingers that have not been chosen to be fingers
- Blue circles represent potential fingers that have been chosen to be fingers


### Thank you for reading
This concludes the manual. Thank you for reading and we hope you enjoy using Type Tutor.


