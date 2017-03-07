#!/usr/bin/python

from pynput import mouse

def on_click(x, y, button, pressed):
    print("{0} at {1}".format(
        "Pressed" if pressed else "Released",
        (x, y)))

def on_scroll(x, y, dx, dy):
    print("Scrolled at {0} by {1}".format(
        (x, y),
        (dx, dy)))

with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
