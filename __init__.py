import math
import pride
import utime
import leds
import display

leds.clear()
display.open().clear().update()

def do_every(delay, func):
    step = 0.0
    while True:
        func(step)
        step = step + delay
        utime.sleep(delay)

def flag_old(step, period):
    brightness = math.sin(float(step)/float(period))*0.5 + 0.5
    print(brightness);
    pride.show_leds("rainbow", brightness=brightness)

def flag(sec_since_start, period):
    brightness = 0.5*math.cos(math.pi*sec_since_start) + 0.5
    print((sec_since_start, brightness))
    pride.show_leds("rainbow", brightness=brightness)


pride.show_display("rainbow", brightness=0.5)
do_every(0.1, lambda sec: flag(sec, 5.0))
