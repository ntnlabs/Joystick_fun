from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import sys

x = 3
y = 3
sense = SenseHat()
sense.low_light = True

def clamp(value, delta):
    if (value+delta)<0:
        return 7
    elif (value+delta)>7:
        return 0
    return value+delta

def pushed_button(event):
    if event.action != ACTION_RELEASED:
        sys.exit()

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y,-1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y,1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x,-1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x,1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 255, 255, 255)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_button
sense.stick.direction_any = refresh
refresh()
pause()
