#!/usr/bin/env python

# Author: Donald L. Merand
# Description: This is the control script for the "Compliment Bot". It looks
# for a button press on the Raspberry Pi's GPIO pin, and when it detects one it
# generates a compliment, and sends it to a serially-connected thermal printer.
# Meanwhile an Arduino makes other robot functions go crazy, such as lighting
# up LEDs, and potentially in the future making sounds, moving motors, etc.

import RPi.GPIO as GPIO
import random
import os
from time import sleep

# use Raspberry Pi pin numbers
#GPIO.setmode(GPIO.BOARD)
# use GPIO numbers not pin numbers (which we will be doing here)
GPIO.setmode(GPIO.BCM)

# this is the button, and the LED inside the buttom
led_pin = 25
button_pin = 24
# set up an arduino to listen on pin 23 using the "compliment-bot-arduino"
# sketch
arduino_pin = 23

# set up the GPIO channels - one input and one output
GPIO.setup(button_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(arduino_pin, GPIO.OUT)

# turn the LED and Arduino "channel" off
GPIO.output(led_pin, False)
GPIO.output(arduino_pin, False)

while True:
  if ( GPIO.input(button_pin) == False ):
    GPIO.output(led_pin, True)
    # tell the arduino to start lighting things up real nice
    GPIO.output(arduino_pin, True)
    # um... this is hard-coded. jeez.
    cmd = "/home/pi/git/compliment-robot/bin/robot -l /home/pi/git/compliment-robot/db"
    os.system(cmd)
    GPIO.output(led_pin, False)
    GPIO.output(arduino_pin, False)
