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
	# Light the appropriate lights
	#
	checkLights()

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
			if( checkButton(black) ):
				# the black button is pressed. Announce the time
				#
				sayCurrentTime()

			if( checkButton(red) ):
				# the red button is pressed. Do something fun
				#
				n = rand()
				if( n==0 ):
					sayWeather()
				elif( n==1 ):
					sayJoke()
				elif( n==2 ):
					playSong()

	# sleep for a brief period, then loop again
	time.sleep(delay)
