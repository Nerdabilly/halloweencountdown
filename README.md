# Raspberry Pi Animated LED Matrix Halloween Countdown 

For the past couple years, I've had a "Countdown to Halloween" sign posted outside my house from the start of September until the day after Halloween. The original design was manual, which required me to go outside and flip the numbers every day. This could get difficult, since sometimes I'd forget and I'd often be fixing or adjusting it if the weather blew the numbers around. I'd always considered it a small and minor part of the display, but I was surprised to learn that my neighbors loved it, so I started coming up with a way to automate the process (and do it with some style).

This project is the code, materials list, and assembly tutorial. It was in progress and well underway when I learned that Adafruit has a [project and purpose-built kit](https://learn.adafruit.com/halloween-countdown-display-matrix) for exactly this, but I didn't want to stop, and why not offer a different option with some more customization?

The specific setup here is using the materials I used, which was a 32x32 LED matrix and a Pi Zero W/Matrix Bonnet combination. Other hardware combinations such as a larger or different aspect ratio matrix or the HAT should also work, but you would have to modify the LED software installation and most likely rebuild the animations and numbers to accomodate those changes. I can't offer support for any of those variations, but they should work as long as you build for what you have.

## Prerequisites

You should have some familiarity with setting up and configuring a headless Raspberry Pi, including adding hardware and flashing/installing the operating system. 

You should also be familiar with pulling Python code libraries from Git onto your Pi (you're here, so you probably know what you're doing with that...)

## Materials

**For this project you will need:**

- a Raspberry Pi (I used an old Pi Zero W I had, but any Pi 4 should work as long as your matrix hardware supports it. Note that a Pi 5 is not ideal here since the current LED Matrix hardware does not support it)
- The LED Matrix [Pi Bonnet](https://www.adafruit.com/product/3211) or [HAT](https://www.adafruit.com/product/2345) (since I was using a Zero, I went with the bonnet, but the HAT should work too. Just use the best one for your Pi board and configure it accordingly) 
- a [32x32 LED Matrix](https://www.adafruit.com/product/2026) (pitch doesn't really matter, pick the one that suits your needs) 
- Power supplies for the Pi and [Matrix](https://www.adafruit.com/product/1466)
- [GPIO ribbon cable](https://www.adafruit.com/product/4170) for connecting the matrix 
- Any additional components or headers for attaching the LED hardware to the Pi (I used a solderless header kit, your specific needs may vary)

That's all you need to get started. I'm including optional stuff below for how I weatherproofed and diffused it, but that's not necessary to simply build the project.

## Getting Started

First, assemble the Pi and Matrix hardware according to the instructions for what you're using. This will vary depending on what Pi and matrix hardware you have, so I'm leaving out the specifics, but the information should be easy to find from Adafruit product pages for the hardware you have.

The [rpi-rgb-led-matrix repo](https://github.com/hzeller/rpi-rgb-led-matrix) goes into some more detail about the best choices for OS and other considerations, so there is a good place to start. Install this library onto your Pi. That should be all you need to get started.

## The Code

The `main.py` file contains everything the countdown needs to run, including the code for pulling randon animations in between displaying the numbers of the countdown, and determining which number to display. To see the countdown in action, simply run that file:

`sudo python3 main.py`

The `display_gif.py` file is imported into the main file and handles the specifics of displaying an animated GIF on the matrix. You shouldn't need to make any changes to it, but it is also a very handy utility if you want to try to create and display GIFs other than the included ones on your matrix:

`sudo python3 display_gif.py yourgif.gif`

## Customization 

There are 3 variables at the top of `main.py` that can be adjusted to tweak the behavior of the countdown:

`SECONDS_TO_DISPLAY_NUMBER`: How long to show the number of days until Halloween on the matrix, in seconds  
`SECONDS_TO_DISPLAY_IMAGE`: How long to show an animation on the matrix in between showing numbers, in seconds

`NUMBERS`: the folder containing the series of animated GIF numbers to display. There are 4 included styles here, in folders `numbers`, `numbers2`, `numbers3`, and `numbers4`. Simply set this variable to the folder containing the style you want. 

You could use `display_gif.py` to preview each style on the matrix, but I find it easier to just open the GIF on your desktop. If you'd like to make your own numbers instead, I've included some tips for that below.

## The Images

This entire project is simply cycling a series of animated GIFs onto the matrix. Everything you see on the matrix - including the number of days - is an animated GIF. The `numbers` folders contain a series of GIFs for every number from 0-365. The `animations` folder is a series of spooky Halloween-themed animations to show at intervals between the countdown numbers. After all, it's an LED matrix, why waste it on just showing some numbers?

The animations in the `animations` folder were found from various sources around the Web and in some cases, optimized to display on the 32x32 Matrix. I did not create them, though they were all available from free, non-attribution and CC0-licensed sources.

If you'd like to create your own or edit and optimize an existing GIF, you can use almost any graphics software (Photoshop, GIMP, etc) to create them, but remember that the matrix is actually very low resolution so you need to be careful with shadows, antialiasing, and too much color depth or variation. I found that [Piskel](https://www.piskelapp.com/) worked best for this, since it specializes in creating low-res "sprite style" GIF animations, which is exactly what this project needs.

## Running as a Service

You probably want this project to run as soon as it's plugged in, so you don't have to constantly open an SSH terminal to start it up. The easiest and most reliable way I found to do this is to set it up as a Linux service. 

See [this Gist](https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f) for detailed instructions on how to do that.

Create a file called `countdown.service` in `/lib/systemd/system/` and have it start the `main.py` script. 

If you ever need to start/stop it for any reason, simply use `systemctl`:

`sudo systemctl stop countdown.service`  
`sudo systemctl start countdown.service`

## OPTIONAL: Making Your Own Numbers

## OPTIONAL: Weatherproofing
