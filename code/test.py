import keyboard #Using module keyboard
while True:  #making a loop
    try:  #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed(' '): #if key space is pressed.You can also use right,left,up,down and others like a,b,c,etc.
            print('You Pressed A Key!')
            break #finishing the loop
    except:
        pass
