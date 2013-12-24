# threads.py
#
# Custom thread classes for running other processes

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
				greenLight(self.blinkState)
				yellowLight(self.blinkState)
				redLight(self.blinkState)

				self.blinkState = not self.blinkState

			# delay
			#
			time.sleep(delay)

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



# A thread class for speaking a series of lines
#
class SpeechThread (threading.Thread):

	def __init__(self, lines):
		threading.Thread.__init__(self)
		self.lines = lines
		self.stopFlag = False

	def run(self):
		for l in self.lines:
			# has the stop flag been set? if so, return
			#
			if( self.stopFlag ):
				return

			# say the next line
			#
			say(l)

	def stop(self):
		self.stopFlag = True



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
			"mpg123",
			"-q",
			songs[i]
		])


	def stop(self):
		# find the PID
		#
		pid = subprocess.check_output(["./scripts/getMpg123PID"])

		# kill the process
		#
		call(["kill", pid.strip()])
