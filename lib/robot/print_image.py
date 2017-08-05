#!/usr/bin/env python

import Image, os, sys
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
printer.begin(75)    # Increase the heat

image_path = sys.argv[1]
os.system('convert ' + image_path + ' -resize 382x764 tmp.png')
printer.printImage(Image.open('tmp.png'), True)
printer.feed(2)
os.system('rm tmp.png')

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
