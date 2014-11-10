#!/usr/bin/env python

from Adafruit_Thermal import *
import sys

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
printer.setDefault() # Restore printer to defaults

printer.setSize('S') # Small font size

# Print out what was piped in
text = sys.stdin.read() 
printer.println(text)
printer.feed(3)

printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
