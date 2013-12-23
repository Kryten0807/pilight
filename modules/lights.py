# lights.py
#
# functions associated with lights
#

import datetime

def checkLights():
	# get the current time
	#
	currentTime = datetime.datetime.time(datetime.datetime.now())

	# check the time
	#
	if( currentTime>=yellowLightOn and currentTime<greenLightOn ):
		# yellow light on, other lights off
		greenLight(False)
		yellowLight(True)
		redLight(False)
	elif( currentTime>=greenLightOn and currentTime<redLightOn ):
		# green light on, other lights off
		greenLight(True)
		yellowLight(False)
		redLight(False)
	else:
		# red light on, other lights off
		greenLight(False)
		yellowLight(False)
		redLight(True)



# @todo write functions to turn lights on/off
def greenLight(state):
	# check the state
	#
	if(state):
		print "G=on"
	else:
		print "G=off"

def yellowLight(state):
	# check the state
	#
	if(state):
		print "Y=on"
	else:
		print "Y=off"

def redLight(state):
	# check the state
	#
	if(state):
		print "R=on"
	else:
		print "R=off"

