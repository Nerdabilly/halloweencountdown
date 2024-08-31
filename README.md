# Raspberry Pi Animated LED Matrix Halloween Countdown 


![newcountdown](https://github.com/user-attachments/assets/32bf50af-8b74-4c1c-8f01-725c6b543c95)

For the past couple years, I've had a "Countdown to Halloween" sign posted outside my house from the start of September until the day after Halloween. The original design was manual, which required me to go outside and flip the numbers every day. This could get difficult, since sometimes I'd forget and I'd often be fixing or adjusting it if the weather blew the numbers around. I'd always considered it a small and minor part of the display, but I was surprised to learn that my neighbors loved it, so I started coming up with a way to automate the process (and do it with some style).

This project is the code, materials list, and assembly tutorial. It was in progress and well underway when I learned that Adafruit has a [project and purpose-built kit](https://learn.adafruit.com/halloween-countdown-display-matrix) for exactly this, but I didn't want to stop, and why not offer a different option with some more customization?

The specific setup here is using the materials I used, which was a 32x32 LED matrix and a Pi Zero W with the Matrix Bonnet. Other hardware combinations such as a larger or different aspect ratio matrix or the HAT should also work, but you would have to modify the LED software installation and most likely rebuild the animations and numbers to accomodate those changes. I can't offer support for any of those variations, but they should work as long as you build for what you have.

## Prerequisites

You should have some familiarity with setting up and configuring a headless Raspberry Pi, including adding hardware and flashing/installing the operating system, and running the Pi terminal over SSH. The projects listed on the Matrix and HAT/Bonnet links below should include everything you need to know to get started with setting up the hardware.

You should also be familiar with pulling Python code libraries from Git onto your Pi (you're here, so you probably know what you're doing with that...)

**Important!** Most versions (maybe all?) of Raspberry Pi do not have an internal clock module. They rely on their Wifi connection to reach out to a date/time server to determine the correct date. This project will give you an inaccurate countdown if it does not have a reliable Wifi connection. There are addon clock modules for Raspberry Pi available, but I haven't used one and didn't create this project with that in mind. So make sure there's a decent wifi connection where you install this. 

Another note - I am a pretty experienced developer with a variety of technologies, but this was actually my first foray into writing anything with Python. I went with Python because that's what the existing Matrix and GIF libraries were written in. This code is simple and it works, but that doesn't mean it's necessarily the best or "most Pythonic" way to do things. If you notice anything, or have any improvements or suggestions, reach out or create an MR. 

## Materials

**For this project you will need:**

- a Raspberry Pi (I used an old Pi Zero W I had, but any Pi 4 should work as long as your matrix hardware supports it. Note that a Pi 5 is not ideal here since the current LED Matrix hardware does not support it)
- The LED Matrix [Pi Bonnet](https://www.adafruit.com/product/3211) or [HAT](https://www.adafruit.com/product/2345) (since I was using a Zero, I went with the bonnet, but the HAT should work too. Just use the best one for your Pi board and configure it accordingly) 
- a [32x32 LED Matrix](https://www.adafruit.com/product/2026) (pitch doesn't really matter, pick the one that suits your needs) 
- Power supplies for the Pi and [Matrix](https://www.adafruit.com/product/1466)
- [GPIO ribbon cable](https://www.adafruit.com/product/4170) for connecting the matrix 
- Any additional components or headers for attaching the LED hardware to the Pi (I used a solderless header kit, your specific needs may vary)
- Reliable Wifi


That's all you need to get started. I'm including optional stuff below for how I weatherproofed and diffused it, but that's not necessary to simply build the project.

## Getting Started

First, assemble the Pi and Matrix hardware according to the instructions for what you're using. This will vary depending on what Pi and matrix hardware you have, so I'm leaving out the specifics, but the information should be easy to find from Adafruit product pages for the hardware you have.

The [rpi-rgb-led-matrix repo](https://github.com/hzeller/rpi-rgb-led-matrix) goes into some more detail about the best choices for OS and other considerations, so that's a good place to start. Install this library onto your Pi. That should be all you need to get started.

## The Code

The `main.py` file contains everything the countdown needs to run, including the code for pulling randon animations in between displaying the numbers of the countdown, and determining which number to display. To see the countdown in action, simply run that file:

`sudo python3 main.py`

The `display_gif.py` file is imported into the main file and handles the specifics of displaying an animated GIF on the matrix. You shouldn't need to make any changes to it, but it is also a very handy utility if you want to try to create and display GIFs other than the included ones on your matrix:

`sudo python3 display_gif.py yourgif.gif`

## Customization 

There are 3 variables at the top of `main.py` that can be adjusted to tweak the behavior of the countdown:

`SECONDS_TO_DISPLAY_NUMBER`: How long to show the number of days until Halloween on the matrix, in seconds  
`SECONDS_TO_DISPLAY_IMAGE`: How long to show an animation on the matrix in between showing numbers, in seconds

`NUMBERS`: the folder containing the series of animated GIF numbers to display. There are 4 included styles here, in folders called `numbers_red`, `numbers_green`, `numbers_orange`, and `numbers_flame`. Set this variable to the name of the folder containing the style you want. You can also create your own style. 

You could use `display_gif.py` to preview each style on the matrix, but I find it easier to just open the GIF on your desktop. If you'd like to make your own numbers instead, I've included some tips for that below.

## The Images

This entire project is simply cycling a series of animated GIFs onto the matrix. Everything you see on the matrix - including the number of days - is an animated GIF. The `numbers` folders contain a series of GIFs for every number from 0-366, to account for leap years. The `animations` folder is a series of spooky Halloween-themed animations to show at intervals between the countdown numbers. After all, it's an LED matrix, why waste it on just showing some numbers?

The animations in the `animations` folder were found from various sources around the Web and in some cases, optimized to display on the 32x32 Matrix. I did not create them, though they were all available from free, non-attribution and CC0-licensed sources.

If you'd like to create your own or edit and optimize an existing GIF, you can use almost any graphics software (Photoshop, GIMP, etc) to create them, but remember that the matrix is very low resolution at only 32px x 32px, so you need to be careful with shadows, antialiasing, and too much color depth or variation. I found that [Piskel](https://www.piskelapp.com/) worked best for this, since it specializes in creating low-res "sprite style" GIF animations, which is exactly what this project needs.

## Running as a Service

You probably want this project to run as soon as it's plugged in, so you don't have to constantly open an SSH terminal to start it up. The easiest and most reliable way I found to do this is to set it up as a Linux service. 

See [this Gist](https://gist.github.com/emxsys/a507f3cad928e66f6410e7ac28e2990f) for detailed instructions on how to do that.

Move the included `countdown.service` file into `/lib/systemd/system/`. 

Make sure you edit this file to use your system username and point to the correct location of the `main.py` script. 

If you ever need to start/stop it for any reason, simply use `systemctl`:

`sudo systemctl stop countdown.service`  
`sudo systemctl start countdown.service`

## OPTIONAL: Making Your Own Numbers

_(There should be no need to go through these next steps unless you want to generate your own images using different fonts or colors than the included options.)_

All of the numbers in the countdown, from 0 to 366, were generated using ImageMagick and a shell script (`generate.sh`, included here) to create them. 

ImageMagick is a very robust, powerful and complicated software, so I'm not going to go into detail on how to use it, other than to explain what the specific calls to it are doing and some tips I learned along the way.

Generating a series of 366 animated images in a loop can be time-consuming, so the better your computer and graphics card is, the faster this will go. 

**Important!** Perform these steps _on your computer_, not on the Pi you will be running this project on, then transfer the images to the Pi memory when you're done. 

To get started:

1. Install [ImageMagick](https://imagemagick.org/)
1. Create a new directory and move `generate.sh` into it 
1. Create 2 new subfolders:
- `tmp_numbers`
- `numbers_output`

Here is where things get tricky, and I can only offer generic advice because it will all vary based on what font you are using, what size matrix you are using, and how big you want the numbers. 

Modify Line 24 of `generate.sh` to use the font and color/gradient you want on the text. 

`magick -size 32x32 xc:black **-font Trade-Winds** -pointsize $(($pointsize + $(($pt)))) -fill gradient:#00ff00 -gravity center -draw "text 0,0 '$index'" tmp_numbers/$index-$frame.gif`

Note that calls to ImageMagick use the system font name, which may not be what displays in your Font Book/Font Explorer when you preview a font. On Mac OS, you can see these by running `identify -list font` in the Terminal. 

This will generate 3 frames of animation and place them into the `tmp_numbers` subfolder. 

The final animation is generated on Line 28 of `generate.sh`:

`magick -size 32x32  -dispose previous -delay 17  -loop 0 tmp_numbers/$index-%d.gif[0-4] -duplicate 1,-2-1   numbers_output/$index.gif`

Again, you may have to play with these values to get the final result you want. 

One helpful tip: if you just want to see one image, edit Line 2 and change:

`for index in $(seq 0 366) `  
to  
`for index in $(seq 0 1)`  

This will generate only one number animation and run a lot more quickly so you can preview your work. 

Another option for previewing is to use only the first ImageMagick command to generate a preview at the Terminal:

`magick -size 32x32 xc:black -font Trade-Winds -pointsize 15 -fill gradient:#00ff00 -gravity center -draw "text 0,0 '$index'" preview.gif`

Once this is done, you can preview the image by just opening it on your desktop (which doesn't always give a good idea of how it will look on the matrix), or copy to the Pi filesystem and use the `display_gif` command (see above) to preview it on the Matrix. 

After you have completed creating the custom numbers, simply copy all of them over the Pi in their own folder and set the `NUMBERS` variable to that folder. You can use `scp` for this, but I found `sshfs` to be faster and easier. 

## OPTIONAL: Weatherproofing

Since my matrix was going to spend 2 months outdoors in increasingly-bad fall weather, I wanted an option for weatherproofing it. After looking into a lot of different possibilities, here is what I can up with. As always, this isn't strictly necessary, especially if your matrix won't be outdoors, and you are welcome to use your own weatherproofing solutions depending on your needs, but I am documenting what I did here for posterity. 

Materials:

- a weatherproof box with a clear cover (I really like [this one from Hawk USA](https://www.hawkusa.com/manufacturers/bud/enclosures/nbf-32414) - it was almost the perfect size for my LED matrix)
- a PG7 [Cable Gland](https://a.co/d/cBcMhjm)
- 4-pin [Low Voltage Wire](https://a.co/d/cBcMhjm)
- [Micro USB Pigtail](https://a.co/d/j2tZsGF) - Originally I did this with Screw Terminal connections, but they were too unreliable
- [Barrel Connector Pigtails](https://a.co/d/0jiUitL) - One Female, One Male
- a [SockitBox](https://a.co/d/1cQADuA) for the Pi and Matrix power sources

Drill a hole in the bottom of the enclosure and install the cable gland and low voltage wire (Make sure you have a plan for how/where it's getting installed and drill the hole/run the wire accordingly! You don't want the wire lead getting in the way of installation. The clear lid of the box is facing forward so you can see the matrix, which means the "bottom" where I made the cord hole is actually the side.):
![image](https://github.com/user-attachments/assets/b94bae4f-21f1-4f86-9a5d-ee72708ce3bf)

Using the Solder Seal connectors, connect the Micro USB pigtail and the Male Barrel connector pigtail to the pins inside the wire. (you will have do the normal red/black on one and use white/yellow for the other. Doesn't really matter as long as your polarity is correct and you make sure the other end is connected the same way.) 
![image](https://github.com/user-attachments/assets/a6ba113c-10fa-4eb8-9282-a2c9a8baa2a1)

Do the same at the other end with the female Barrel Connector and the USB A Male Connector (again, watch your polarity! you will need to use white/yellow to connect red/black on one of them. Just keep track of what's going where. I used yellow to connect to red and white to connect to black on the matrix power cord)
![image](https://github.com/user-attachments/assets/35ffbfb3-7dbe-4a4f-89b1-24303c23c3e8)

The Pi and Matrix will stay inside the enclosure. The Matrix is held in place up against the screen using a bracked that I 3D printed (included in the repo in the `stl` folder):

Store the power supplies for the Pi and the Matrix inside the SockitBox. 

Run an outdoor extension cord into the SockitBox and run the 4-pin wire out of the SockitBox to connect the Matrix enclosure.


## OPTIONAL: Diffusing with Diffusion Acrylic 

You can use [Black Diffusion Acrylic](https://www.adafruit.com/product/4594) to diffuse the LED lights on the Matrix. 

This isn't strictly necessary although it does help make the image a little cleaner-looking and less eye-hurty. I cut it down to size with a table saw and [this saw blade](https://a.co/d/cDQalF4).

