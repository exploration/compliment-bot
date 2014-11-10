# Compliment Robot

It gives you compliments.

## Command Line Operation

`./compliment.py` runs the program. The program monitors a button plugged into a GPIO pin on the RPi. When the button is pressed, it lights up a LED (inside the button), activates an Arduino which does fancy things like light up LEDs, and maybe run some motors or whatever, and also prints out a compliment to the thermal printer.



## Full Raspberry Pi Setup

(from a machine on the same LAN as the raspberry pi. you can skip the `ssh` steps if you're running locally on the Pi with a connected monitor keyboard etc.)

- install [raspberry pi distro](http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2)
- connect to network (or computer sharing internet over ethernet)
- `ssh pi@raspberrypi.local` - password is 'raspberry'
- (on the Pi now) `sudo raspi-config
    - change password
    - expand filesystem if using a >4GB card
    - set locale properly (en-us-utf8 for us on the east coast USA)
    - update software
    - exit
- `sudo reboot`
- `ssh pi@raspberrypi.local` again
- `sudo apt-get update`
- `sudo apt-get install python-serial python-imaging python-unidecode ruby1.9.3 figlet git`
- edit /boot/cmdline.txt
    - change `dwc_otg.lpm_enable=0 console=ttyAMA0,115200 kgdboc=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait` to...
    - `dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait`
- `mkdir ~/git && cd ~/git && git clone https://github.com/exploration/compliment-bot.git`
- `sudo reboot`
- connect printer ground (black) to [GPIO](http://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/) ground (pin 6).
- connect printer "rx" (yellow) to GPIO14 (pin 8)
- `ssh pi@raspberrypi.local`
- `cd git/compliment-robot`
- `./compliment.py`
  - OR you could edit /etc/rc.local and add the line `cd ~/git/compliment-robot && ./compliment.py`, which would make the program run on system start.
