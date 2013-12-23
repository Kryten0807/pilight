# constants.py
#
# Contains the constant values for the various parts of the pilight script

# the child's name
#
childsName = "Robert"



# GPIO pin numbers
#
redButton   = 1
blackButton = 2

greenLight  = 3
yellowLight = 4
redLight    = 5

# time values
# These are the times at which to turn on the appropriate lights
#

import datetime

greenLightOn  = datetime.time(7,0,0)
yellowLightOn = datetime.time(6,30,0)
redLightOn    = datetime.time(19,0,0)


# the "inactivity" period, in seconds
#
inactiveTime = 2 * 3600;	# 2 hours
