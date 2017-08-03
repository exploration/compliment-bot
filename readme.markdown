# Compliment Robot

It gives you compliments, on little pieces of paper.

Author: Donald L. Merand for [Explo](http://www.explo.org/)

![example build](help/example-build/compliment-bot-v1.png)
![example build - internals](help/example-build/compliment-bot-v1-internals-1.png)
![example build - closeup](help/example-build/compliment-bot-v1-internals-2.png)


## License

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).


## Operation

`./compliment.py` (from the command line) runs the program. The program monitors a button plugged into a GPIO pin on the RPi. When the button is pressed, it lights up a LED (inside the button), activates an Arduino which does fancy things like light up LEDs, and maybe run some motors or whatever, and also prints out a compliment to the thermal printer.


## Full Setup

### On the Raspberry Pi

(from a machine on the same LAN as the raspberry pi. you can skip the `ssh` steps if you're running locally on the Pi with a connected monitor keyboard etc.)

- install [raspberry pi distro](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2)
- connect to network (or computer sharing internet over ethernet)
- `ssh pi@raspberrypi.local` - password is 'raspberry'
- (on the Pi now) `sudo raspi-config`
    - change password
    - expand filesystem if using a >4GB card
    - set locale properly (en-us-utf8 for us on the east coast USA)
    - update software
    - exit
- `sudo reboot`
- `ssh pi@raspberrypi.local` again
- `sudo apt-get update`
- `sudo apt-get install python-serial python-imaging python-unidecode ruby1.9.3 figlet git`
- edit /boot/cmdline.txt (to enable serial connection to the thermal printer)
    - change `dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait` to...
    - `dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait`
- `mkdir ~/git && cd ~/git && git clone https://github.com/exploration/compliment-bot.git`
- `sudo reboot`


### On the Arduino

This part is easy, all you have to do is use the [Arduino IDE](http://arduino.cc/en/Main/Software) to upload the `compliment-bot-arduino.ino` sketch.


### Wire It Together

Here is the [Bill of Materials](https://docs.google.com/spreadsheets/d/1Q8_7Lmra2s3A8SbT2oduA7fXXXVdrU4QU93FSB4Z0Tc/edit?usp=sharing) necessary to wire the project together. Expect to spend in the neighborhood of $150-$200, depending on what you have lying around.

Here is the [Adafruit Trinket](https://www.adafruit.com/products/1500) version of the wiring diagram:
![wiring diagram](help/wiring-diagrams/compliment-bot-wiring-trinket_bb.png)

- [GPIO reference for the Raspberry Pi Model B+](https://learn.adafruit.com/introducing-the-raspberry-pi-model-b-plus-plus-differences-vs-model-b/gpio-port)


### Run the Program

- `ssh pi@raspberrypi.local`
- `cd git/compliment-robot`
- `./compliment.py`
  - OR you could edit `/etc/rc.local` and add the line `cd /home/pi/git/compliment-robot && sudo ./compliment.py`, which would make the program run on system start.



# PS

You can visit compliment bot [online](http://robot.lab.explo.org) if you want to :)
