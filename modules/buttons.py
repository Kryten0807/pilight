# buttons.py
#
# Functions related to buttons

import os.path
import time
import json

# check the state of a button
#
def checkButton(b):
	# @todo check the GPIO state
	#
	return False;

def getLastButtonPress():
	# does the file 'storage/lastButtonPress' exist? if not, return 0
	#
	if( not os.path.exists('storage/lastButtonPress') ):
		return 0

	# load the file
	#
	with open('storage/lastButtonPress') as f:
		return json.load(f)

def setLastButtonPress():
	# get the current time
	#
	#currentTime = datetime.datetime.time(datetime.datetime.now())

	# save the data
	#
	t = time.time()
	with open('storage/lastButtonPress', 'w') as f:
		json.dump(t, f)

def secondsSinceLastButtonPress():
	# get the last button press time
	#
	t0 = getLastButtonPress()

	# get the current time value
	#
	t1 = time.time();

	# return the difference
	#
	return t1 - t0

def waitForAnyButton():
	# a counter to stop the waiting if nothing happens
	#
	n = 0;

	while n<timeout:
		if( checkButton(redButton) or checkButton(blackButton) ):
			return True

		time.sleep(delay)

		n = n + delay

	return False

def waitForRedButton():
	# a counter to stop the waiting if nothing happens
	#
	n = 0;

	while n<timeout:
		if( checkButton(redButton) ):
			return True

		time.sleep(delay)

		n = n + delay

	return False
