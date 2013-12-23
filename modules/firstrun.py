# firstrun.py
#
# functions  related to the "first run" functionality

import threading

# is this the first run of the application?
#
def isFirstRun():
	return not os.path.exists('storage/firstRun')

# set the "first run" flag
#
def setFirstRunFlag():
	# write something into the file
	#
	with open('storage/firstRun', 'w') as f:
		f.write('')

# go through the introduction routine
#
def introduction():
	# say the opening introduction speech
	#
	sayIntroduction()

	# wait for a button
	#
	b = waitForAnyButton()
	if( not b ):
		return

	# start blinking the lights
	# threading code from http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
	# if this doesn't work, try http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
	#
	t = threading.Thread(target=blinkAll, args=())
	t.start()

	# say the instructions
	#
	sayLightInstructions()

	# stop blinking the lights
	#
	continueBlinking = False

	# wait for a button
	#
	b = waitForAnyButton()
	if( not b ):
		return

	# say the button instructions
	#
	sayButtonInstructions()

	# reset the lights
	#
	checkLights()

	# wait for the red button
	#
	b = waitForRedButton()
	if( not b ):
		return

	# play a song
	#
	playSong()


