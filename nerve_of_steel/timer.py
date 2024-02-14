# This program is a countdown_timer used for Nerve of Steel Game


import time # The time library has a sleep function that will pause the script for a specifized amount of time
from PIL import Image # the pillow library makes it easy to display images 

im = Image.open("times-up.jpeg")

def display_countdown(num):
    print("\r{:02d}".format(num), end='', flush=True)  

def countdown_timer(set_time):
    print("Players, stand!")
    time.sleep(1)
    for t in range(set_time, 0, -1):  
        display_countdown(t)
        time.sleep(1)
    print("\r" + " " * 5, end='\r')  
    print("Times Up! Last to sit down wins.")


# ask user to enter desired countdown time
set_time = int(input("Please set your timer in seconds: "))

if set_time < 5 or set_time > 25:
    print("Error: Duration must be between 5 and 25 seconds.")
else:
    print("Starting countdown...")
    countdown_timer(set_time)
    im.show()

