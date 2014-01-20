# threads.py
#
# Custom thread classes for running other processes

import random
import threading
import time
import subprocess

# A thread class for handling the light state
#
class LightThread (threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.blink = False
		self.blinkState = False

	def run(self):
		# the main loop for the lights
		#
		while True:
			# are we paused? if not, then update the current light state
			#
			if( not self.blink ):
				# set the light state based on the time of day
				#
				checkLights()
			else:
				# the system wants to blink the lights
				#
				setGreenLightOn(self.blinkState)
				setYellowLightOn(self.blinkState)
				setRedLightOn(self.blinkState)

				self.blinkState = not self.blinkState

			# delay
			#
			if( self.blink ):
				time.sleep(delay)
			else:
				time.sleep(lightDelay)

	def blinkOn(self):
		# reset the blink state
		#
		self.blinkState = False

		# set the blink flag
		#
		self.blink = True

	def blinkOff(self):
		# set the blink flag
		#
		self.blink = False

		# reset the blink state
		#
		self.blinkState = False




# A thread class for playing a song
#
class SongThread (threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		# choose a song from the list at random
		#
		i = random.randint(0,len(songs)-1)

		call([
			"mplayer",
			"-quiet",
			songs[i]
		])


	def stop(self):
		# find the PID
		#
		pid = subprocess.check_output([basepath+"/scripts/getMusicPlayerPID"])

		# kill the process
		#
		call(["kill", pid.strip()])
