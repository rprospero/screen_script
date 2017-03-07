#!/usr/bin/python

from pynput import mouse, keyboard

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

    def on_press(key):
        print('key {0} pressed'.format(key))

    def on_release(key):
        print("key {0} released".format(key))
        if key == keyboard.Key.esc:
            listener.stop()
            return False

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as klistener:
        klistener.join()
        listener.join()
