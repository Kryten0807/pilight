# threads.py
#
# Custom thread classes for running other processes

import threading
import time

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

