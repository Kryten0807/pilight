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
	f = open('storage/lastButtonPress')
	return json.load(f)

def setLastButtonPress():
	# get the current time
	#
	#currentTime = datetime.datetime.time(datetime.datetime.now())

	# save the data
	#
	f = open('storage/lastButtonPress', 'w')
	t = time.time()
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
