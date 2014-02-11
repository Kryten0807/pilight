# gpio.py
#
# GPIO functions


# set a pin to output
#
def setGPIOPinOut(pin):
	if( not debug ):
		GPIO.setup(pin, GPIO.OUT)

# change the state of an output pin
#
def setPinState(pin, state):
	if( not debug ):
		GPIO.output(pin, state)


# set a pin to input
#
def setGPIOPinIn(pin):
	if( not debug ):
		GPIO.setup(pin, GPIO.IN)

def getPinState(pin):
	if( not debug ):
		return GPIO.input(pin)

	return None





if( not debug ):
        print "importing gpio"
        import RPi.GPIO as GPIO

        # set the GPIO mode
        #
        GPIO.setmode(GPIO.BCM)

        # the output pins (for the LEDs)
        #
        setGPIOPinOut(greenLightPin)
        setGPIOPinOut(yellowLightPin)
        setGPIOPinOut(redLightPin)

        # the input pins (for the buttons)
        #
        setGPIOPinIn(redButton)
        setGPIOPinIn(blackButton)


