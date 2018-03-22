from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
sense = SenseHat()

def pushed_middle(event):
    if event.action != ACTION_RELEASED:
        print("click")

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        print("up")

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        print("down")

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        print("left")

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        print("right")

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
