#!/usr/bin/python

from pynput import mouse, keyboard
from sys import argv
from time import time

def on_clicker(handle):
    def on_click(x, y, button, pressed):
        handle.write("{0} at {1} @ {2}\n".format(
            "Pressed" if pressed else "Released",
            (x, y),
            time()))
    return on_click

def on_scroller(handle):
    def on_scroll(x, y, dx, dy):
        handle.write("Scrolled at {0} by {1} @ {2}\n".format(
            (x, y),
            (dx, dy),
            time()))
    return on_scroll

def on_presser(handle):
    def on_press(key):
        handle.write('key {0} pressed @ {1}\n'.format(key, time()))
    return on_press

def on_releaser(handle, listener):
    def on_release(key):
        handle.write("key {0} released @ {1}\n".format(key, time()))
        if key == keyboard.Key.esc:
            print("Finished")
            listener.stop()
            return False
    return on_release

print(argv)
start=time()
with open(argv[1], "w") as outfile:
    outfile.write("starttime {0}\n".format(start))
    with mouse.Listener(
            on_click=on_clicker(outfile),
            on_scroll=on_scroller(outfile)) as listener:
        with keyboard.Listener(
                on_press=on_presser(outfile),
                on_release=on_releaser(outfile, listener)) as klistener:
            klistener.join()
