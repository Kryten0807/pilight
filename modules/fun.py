# fun.py
#
# Fun functions

import random
import time

def playSong():
	# the list of songs
	#
	songs = [
		"alpha",
		"beta"
	]

	# choose a song from the list at random
	# @todo the upper bound of this should be the largest index in the songs array
	#
	i = random.randint(0,2)

	# play the song
	# @todo play the song via shell command?
	#

def tellJoke():
	# the list of jokes
	#
	jokes = [
		[ "Why did the chicken cross the road?", "To get to the other side."]
	]

	# say the introduction
	#
	say("Here's a joke for you, "+childsName+".")

	# tell the first part of the joke
	# @todo
	#

	# wait a moment
	#
	time.sleep(3)

	# tell the answer
	# @todo
	#


def giveWeatherReport():
	# get the weather giveWeatherReport
	# @todo
	#

	# parse the result into a simple readable version
	# @todo
	#

	# say the weather report
	# see http://forecast.weather.gov/MapClick.php?lat=34.20540&lon=-119.16813730000001&unit=0&lg=english&FcstType=dwml for a sample weather report as XML
	# @todo
	#

