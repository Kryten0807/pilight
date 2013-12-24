# The main loop

import time
from sys import exit

# load the modules
#
execfile('modules/constants.py')
execfile('modules/gpio.py')
execfile('modules/threads.py')
execfile('modules/lights.py')
execfile('modules/buttons.py')
execfile('modules/firstrun.py')
execfile('modules/speak.py')
execfile('modules/fun.py')


sayCurrentTime()

exit()

# initialize the GPIO state
#
setGPIOMode()

# the output pins (for the LEDs)
#
setGPIOPinOut(greenLight)
setGPIOPinOut(yellowLight)
setGPIOPinOut(redLight)

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
		if( secondsSinceLastButtonPress>inactiveTime ):
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

			if( red and black ):
				if( songThread.isAlive() ):
					songThread.stop()

			elif( black ):
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
					say("I'm going to play a new song for you.")
				else:
					say("I'm going to play a song for you.")

	# sleep for a brief period, then loop again
	time.sleep(delay)
