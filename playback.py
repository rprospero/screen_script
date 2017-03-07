#!/usr/bin/python

import numpy as np
from pynput import mouse, keyboard
import pyscreenshot
from sys import argv
from time import sleep

def run_key(c):
    Key = keyboard.Key
    controller = keyboard.Controller()
    commands = c.split()
    key = eval(commands[1])
    print(key)
    press = commands[2]
    if press == "pressed":
        controller.press(key)
    else:
        controller.release(key)

def run_scroll(c):
    controller = mouse.Controller()
    commands = c.split()
    x = int(commands[2][1:-1])
    y = int(commands[3][:-1])
    dx = int(commands[5][1:-1])
    dy = int(commands[6][:-1])

    controller.position = (x, y)
    controller.scroll(dx, dy)

def run_mouse(c):
    Button = mouse.Button
    controller = mouse.Controller()
    commands = c.split()
    press = commands[0]
    x = int(commands[2][1:-1])
    y = int(commands[3][:-1])
    controller.position = (x, y)
    print(x, y)
    if press == "Pressed":
        print("Press")
        controller.press(Button.left)
    else:
        print("release")
        controller.release(Button.left)

def run_command(c):
    if c.split()[0] == "key":
        run_key(c)
    elif c.split()[0] == "Scrolled":
        run_scroll(c)
    else:
        run_mouse(c)

with open(argv[1], "r") as infile:
    data = infile.readlines()

    starttime = data[0]
    starttime = float(starttime.split(" ")[1])

    data = data[1:]
    times = [float(d.split("@")[1])-starttime
             for d in data]
    times = np.array(times)
    deltas = times[1:]-times[:-1]
    deltas = np.hstack([[0], deltas])

    commands = [d.split("@")[0]
                for d in data]

    for (idx, (c, d)) in enumerate(zip(commands, deltas)):
        sleep(d)
        run_command(c)
        pyscreenshot.grab_to_file("step{:03}.png".format(idx))
