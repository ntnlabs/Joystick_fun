# importing the needed stuff
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import sys

# initial environment setup
sense = SenseHat()
sense.low_light = True

# variable setup
x = 3
y = 3

# function that increments or decrements a variable, with loop functionality (7+1=0)
# value is what we need to change, delta is the change
def clamp(value, delta):
# if we are below 0, lets go around and make it a 7
    if (value+delta)<0:
        return 7
# if we are over 7, lets go around and make it a 0
    elif (value+delta)>7:
        return 0
# if we are not going around, lets just change the number
    return value+delta

# if we push the joystick, we exit the script
def pushed_button(event):
    if event.action != ACTION_RELEASED:
        sys.exit()

# if we push the joystick up, we go up
def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y,-1)

# if we push the joystick down, we go down
def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y,1)

# if we push the joystick left, we go left
def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x,-1)

# if we push the joystick right, we go right
def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x,1)

# refraw the pixel
def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

# define a separate call for every possible joystick move
sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_button

# if any momevent is detected, lets draw the pixel
sense.stick.direction_any = refresh

# lets draw the pixel
refresh()

# wait for joystick input
pause()
