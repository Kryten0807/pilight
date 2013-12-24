# lights.py
#
# functions associated with lights
#

import datetime
import time

# check the time against the configured times and light the appropriate lights
#
def checkLights():
	# get the current time
	#
	currentTime = datetime.datetime.time(datetime.datetime.now())

	# declare a variable to hold the state
	#
	state = ''

	# check the time
	#
	if( currentTime>=yellowLightOnTime and currentTime<greenLightOnTime ):
		# yellow light on, other lights off
		setGreenLightOn(False)
		setYellowLightOn(True)
		setRedLightOn(False)
		state = 'yellow'

	elif( currentTime>=greenLightOnTime and currentTime<redLightOnTime ):
		# green light on, other lights off
		setGreenLightOn(True)
		setYellowLightOn(False)
		setRedLightOn(False)
		state = 'green'

	else:
		# red light on, other lights off
		setGreenLightOn(False)
		setYellowLightOn(False)
		setRedLightOn(True)
		state = 'red'

	# return the state
	#
	return state


def blinkAll():
	# reset the flag
	#
	continueBlinking = True

	# start the loop
	#
	while True:
		# all lights on
		#
		greenLight(True)
		yellowLight(True)
		redLight(True)

		# pause
		#
		time.sleep(delay)

		# all lights off
		#
		greenLight(False)
		yellowLight(False)
		redLight(False)

		# pause
		#
		time.sleep(delay)

		# check the exit condition
		#
		if( not continueBlinking ):
			return

# set the state of the green light
#
def setGreenLightOn(state):
	# set the state
	#
	setPinState(greenLightPin, state)

# set the state of the yellow light
#
def setYellowLightOn(state):
	# set the state
	#
	setPinState(yellowLightPin, state)

# set the state of the red light
#
def setRedLightOn(state):
	# set the state
	#
	setPinState(redLightPin, state)
