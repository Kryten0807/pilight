# pilight.py

# The main loop

import os
import time
from sys import exit

# load the modules
#
basepath = os.path.dirname(os.path.abspath(__file__))

execfile(basepath+"/modules/config-default.py")

if( os.path.exists(basepath+"/modules/config.py") ):
	execfile(basepath+"/modules/config.py")

execfile(basepath+"/modules/gpio.py")
execfile(basepath+"/modules/threads.py")
execfile(basepath+"/modules/time.py")
execfile(basepath+"/modules/lights.py")
execfile(basepath+"/modules/buttons.py")
execfile(basepath+"/modules/firstrun.py")
execfile(basepath+"/modules/speak.py")
execfile(basepath+"/modules/fun.py")



# initialize the GPIO state
#
setGPIOMode()

# the output pins (for the LEDs)
#
setGPIOPinOut(greenLightPin)
setGPIOPinOut(yellowLightPin)
setGPIOPinOut(redLightPin)

# the input pins (for the buttons)
#
setGPIOPinIn(redButton)
setGPIOPinIn(blackButton)

# initialize the light control thread
#
lightThread = LightThread()

# start the light thread
#
lightThread.start()

# declare a song thread variable for later use. If it's set, then we can check
# to see if it's running and stop it if we need to
#
songThread = SongThread()

# start the loop
#
while True:
	# Handle the buttons
	#
	if( checkButton(redButton) or checkButton(blackButton) ):

		# when was the last button pressed? if more than two hours ago,
		# then say the appropriate greeting
		#
		if( secondsSinceLastButtonPress()>inactiveTime ):
			# is this the first run? if so, say the first run greeting and
			# the instructions
			#
			if( isFirstRun() ):
				# run the introduction script
				#
				introduction()

				# set the first run flag
				#
				setFirstRunFlag()

			else:
				# say the usual greeting
				#
				sayGreeting()

		else:
			# the child has been playing with it & has pressed a button
			# recently
			#

			# get the button states
			#
			red = checkButton(redButton)
			black = checkButton(blackButton)

			# handle the individual button presses
			#
			if( black ):
				# the black button is pressed. Announce the time
				#
				sayCurrentTime()

			elif( red ):
				# is a song already playing? if so, stop it & announce that
				# we're going to play a new song. Otherwise, announce that it's
				# time to play a song
				#
				if( songThread.isAlive() ):
					songThread.stop()
					say("I stopped the song.")
				else:
					say("I'm going to play a song for you.")
					songThread = SongThread()
					songThread.start()

		# set the time of the last button press
		#
		setLastButtonPress()

	# sleep for a brief period, then loop again
	time.sleep(delay)
