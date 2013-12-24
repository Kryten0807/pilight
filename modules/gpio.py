# gpio.py
#
# GPIO functions

import RPi.GPIO as GPIO

# set the GPIO mode
#
def setGPIOMode():
	GPIO.setmode(GPIO.BCM)

# set a pin to output
#
def setGPIOPinOut(pin):
	GPIO.setup(pin, GPIO.OUT)

# change the state of an output pin
#
def setPinState(pin, state):
	GPIO.output(pin, state)


# set a pin to input
#
def setGPIOPinIn(pin):
	GPIO.setup(pin, GPIO.IN)

def getPinState(pin):
	return GPIO.input(pin)
