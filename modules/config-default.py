# config.py
#
# Contains the constant values for the various parts of the pilight script

import datetime

# the child's name
#
childsName = "Alberto"


# the delay for the main loop, in seconds
#
delay = 0.25			# 1/4 second

# the delay for the light check loop, in seconds
#
lightDelay = 5


# the timeout value for waits, in seconds
#
timeout = 10 * 60		# 10 minutes


# GPIO pin numbers
#
redButton   = 17
blackButton = 27

greenLightPin  = 25
yellowLightPin = 24
redLightPin    = 23


# time values
# These are the times at which to turn on the appropriate lights
#
greenLightOnTime  = datetime.time(7,30,0)
yellowLightOnTime = datetime.time(7,0,0)
redLightOnTime    = datetime.time(19,0,0)


# the "inactivity" period, in seconds
#
inactiveTime = 2 * 3600;	# 2 hours


# the list of songs available to play
#
songs = []


# the path to the "remote speech" file
#
remoteSpeechFile = ""
