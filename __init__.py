import buttons
import math
import pride
import utime
import leds
import display

leds.clear()
display.open().clear().update()

flags = list(pride.flags)
print(flags)
flag_index = 0
last_pressed = 0

def do_every(delay, func):
    step = 0.0
    while True:
        func(step)
        step = step + delay
        utime.sleep(delay)

def flag(sec_since_start, period):
    global last_pressed, flag_index
    brightness = 0.5*math.cos(math.pi*sec_since_start) + 0.5
    pride.show_leds(flags[flag_index], brightness=brightness)
    pressed = buttons.read(buttons.BOTTOM_RIGHT | buttons.TOP_RIGHT)
    if last_pressed != pressed:
        last_pressed = pressed
        if pressed == buttons.TOP_RIGHT:
            flag_index = (flag_index + 1) % len(flags)
        elif pressed == buttons.BOTTOM_RIGHT:
            flag_index = (flag_index - 1) % len(flags)
        pride.show_display(flags[flag_index], brightness=0.5)

pride.show_display(flags[flag_index], brightness=0.5)
do_every(0.1, lambda sec: flag(sec, 5.0))
