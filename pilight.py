# The main loop

import time
from sys import exit


# load the modules
#
execfile('modules/constants.py')
execfile('modules/lights.py')
execfile('modules/buttons.py')
execfile('modules/firstrun.py')
execfile('modules/speak.py')


sayButtonInstructions()

exit()

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
				sayIntroduction()
				sayInstructions()
				# set the first run flag
				#
				setFirstRunFlag()
			else:
				sayGreeting()
		else:
			# the child has been playing with it & has pressed a button
			# recently
			#
			if( checkButton(red) ):
				# the red button is pressed. Announce the time
				#
				sayCurrentTime()
			if( checkButton(black) ):
				# the black button is pressed. Do something fun
				#
				switch( rand() )
					case 1:
						sayWeather()
					case 2:
						sayJoke()
					case 3:
						playSong()
					case 4:
						sayNiceThing()

	# sleep for a brief period, then loop again
	time.sleep(delay)
