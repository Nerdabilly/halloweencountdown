import glob
import os
from webbrowser import get
from display_gif import display_gif
import datetime
import asyncio
import random
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

SECONDS_TO_DISPLAY_NUMBER = 8 # number of seconds to show a number, change this if you want the numbers up for longer or shorter time
SECONDS_TO_DISPLAY_IMAGE = 3 # number of seconds to show the animations

# NUMBERS: name of the folder where the countdown number GIFs are.
# Included values are : `numbers_red`, `numbers_green`, `numbers_orange`, and `numbers_flame`.
# See README.md for additional customization information

NUMBERS = "numbers_red"  

folder =  NUMBERS
days_until_halloween = 0
basepath = "/home/christopherault/"

def display_image(path):
    global folder
    loop = asyncio.get_event_loop()
    seconds = SECONDS_TO_DISPLAY_NUMBER if (folder==NUMBERS) else SECONDS_TO_DISPLAY_IMAGE
    print("seconds " + str(seconds))
    task = loop.create_task(display_gif(path, seconds))
    complete = loop.run_until_complete(task)

    if complete:
        print(f" Image display completed! - {complete}")
        display_next_image()

def display_next_image():
    path = get_next_image()
    display_image(path)


def begin():
    days_until_halloween = get_days_until_halloween()
    print (f"{days_until_halloween} days until Halloween!")
    display_image(os.path.dirname(__file__) + "/" + folder + "/" + str(days_until_halloween) + ".gif" )

def get_next_image():
    global folder
   
    folder = "animations" if (folder == NUMBERS) else NUMBERS

    if folder == "animations":
     
        animations = os.listdir(basepath + "animations")
        animation = random.choice(animations)        
        
        # make sure we selected a gif 
        while '.gif' not in animation: 
            animation = random.choice(animations)

        print("animation about to play: " + animation)
        path = folder + "/" + animation
    else:
        folder = NUMBERS
        days_until_halloween = get_days_until_halloween()
        path = folder + "/" + str(days_until_halloween) + ".gif" 
    return basepath + "/" + path 

def get_days_until_halloween():
    today = datetime.date.today()
    year = today.year

    if today.month > 10:
        year += 1
    future = datetime.date(year,10,31)
    diff = future - today
    return diff.days

begin()


