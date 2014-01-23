# firstrun.py
#
# functions  related to the "first run" functionality


import threading


# is this the first run of the application?
#
def isFirstRun():
	return not os.path.exists(basepath+'/storage/firstRun')


# set the "first run" flag
#
def setFirstRunFlag():
	# write something into the file
	#
	with open(basepath+'/storage/firstRun', 'w') as f:
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

	# say the instructions
	#
	sayLightInstructions()

	# wait for a button
	#
	b = waitForAnyButton()
	if( not b ):
		return

	# say the button instructions
	#
	sayButtonInstructions()

	# say the button instructions
	#
	sayFinalInstructions()

	# set the "first run" flag
	#
	setFirstRunFlag()


