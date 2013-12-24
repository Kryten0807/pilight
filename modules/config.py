# config.py
#
# Contains the constant values for the various parts of the pilight script

import datetime

# the child's name
#
childsName = "Robert"


# the delay for the main loop, in seconds
#
delay = 0.25			# 1/4 second


# the timeout value for waits, in seconds
#
timeout = 10 * 60		# 10 minutes


# GPIO pin numbers
#
redButton   = 17
blackButton = 27

greenLightPin  = 23
yellowLightPin = 24
redLightPin    = 25


# time values
# These are the times at which to turn on the appropriate lights
#
greenLightOn  = datetime.time(7,0,0)
yellowLightOn = datetime.time(6,30,0)
redLightOn    = datetime.time(19,0,0)


# the "inactivity" period, in seconds
#
inactiveTime = 2 * 3600;	# 2 hours


# a flag used for the blinking light function to signal when it's time to stop
#
continueBlinking = False


# the list of songs available to play
#
songs = [
	"/path/to/song1.mp3",
	"/path/to/song2.mp3",
	"/path/to/song3.mp3",
]
