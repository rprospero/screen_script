#!/usr/bin/python

from pynput import mouse, keyboard
from sys import argv

def on_clicker(handle):
    def on_click(x, y, button, pressed):
        handle.write("{0} at {1}\n".format(
            "Pressed" if pressed else "Released",
            (x, y)))
    return on_click

def on_scroller(handle):
    def on_scroll(x, y, dx, dy):
        handle.write("Scrolled at {0} by {1}\n".format(
            (x, y),
            (dx, dy)))
    return on_scroll

def on_presser(handle):
    def on_press(key):
        handle.write('key {0} pressed\n'.format(key))
    return on_press

def on_releaser(handle, listener):
    def on_release(key):
        handle.write("key {0} released\n".format(key))
        if key == keyboard.Key.esc:
            listener.stop()
            return False
    return on_release

print(argv)
with open(argv[1], "w") as outfile:
    with mouse.Listener(
            on_click=on_clicker(outfile),
            on_scroll=on_scroller(outfile)) as listener:
        with keyboard.Listener(
                on_press=on_presser(outfile),
                on_release=on_releaser(outfile, listener)) as klistener:
            klistener.join()
            listener.join()
