# -*- coding: utf-8 -*-
"""
A countdown timer that loops.
"""

import keyboard
import time
def countdown(t):
        while t > 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print(t)
            t -= 1
            time.sleep(1)
            if keyboard.is_pressed("\\"):
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nResetting in "+sleepstr+" seconds!")
                time.sleep(sleeps)
                countdown(seconds)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNext in "+sleepstr+" seconds!")
        time.sleep(sleeps)
        countdown(seconds)


print("Press the backslash during countdown to reset.\n\nClose the program to select a new countdown length.\n\nHow many seconds to count down from?\nEnter an integer:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer:")
    seconds = input()
    
print("Set the time between count downs.\nEnter an integer:")
sleeps = input()
while not sleeps.isdigit():
    print("That wasn't an integer! Enter an integer:")
    sleeps = input()

seconds = int(seconds)
sleeps = int(sleeps)
sleepstr = str(sleeps)
countdown(seconds)
