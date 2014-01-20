# speak.py
#
# speech related functions

import random
from subprocess import call
from time import localtime, strftime


# say a line of text
#
def say(text):
	# say the text
	#
	call([ 'python', basepath+"/scripts/cspeak.py", text ])



# say a collection of lines
#
def sayLines(lines):
	# step through the lines
	#
	for l in lines:
		say(l)



def sayGreeting():
	# say the greeting
	# @todo make this more fun - personalized, based on time of day, etc.
	#
	lines = []

	i = random.randint(1,3)
	if( i==1 ):
		lines.append("Hello "+childsName+".")
	elif( i==2 ):
		lines.append("Good morning "+childsName+".")
	else:
		lines.append("Hi "+childsName+".")

	lines.append("What would you like to do next?")

	sayLines(lines)



def sayCurrentTime():
	# get the current time
	#
	t = strftime("%I:%M", localtime())

	# build the list of lines to speak
	#
	lines = ["It is now "+t+"."]

	# add the state of the lights (ie. not time to get up yet)
	state = checkLights()

	if( state=='green' ):
		lines.append("It's time to get up.")
	elif( state=='yellow' ):
		lines.append("It's almost time to get up, but not yet.")
	else:
		lines.append("It's not time to get up.")

	sayLines(lines)



def sayIntroduction():
	lines = [
		"Hello "+childsName+".",
		"I'm your new talking clock.",
		"Would you like me to tell you how I work?",
		"Press the red button or the black button."
	]

	for l in lines:
		say(l)


def sayLightInstructions():
	# start blinking the lights
	#
	lightThread.blinkOn()

	# the lines to say
	#
	lines = [
		"Great. Thank you "+childsName+".",
		"Look at the top of my box. You'll see three big round lights.",
		"I'm blinking them now.",
		"One is green.",
		"One is yellow.",
		"And one is red.",
		"When the green light is on, it's time to go see mommy and daddy in their room.",
		"When the red light is on, that means it's time to stay in your room.",
		"And when the yellow light is on, that means it's almost time to go see mommy and daddy.",
		"But it's not time yet.",
		"Do you understand, "+childsName+"?",
		"Green means go see mommy and daddy.",
		"Red means stay in your room.",
		"And yellow means it's almost time to get up.",
		"Thanks for listening, "+childsName+".",
		"Press a button and I'll tell you more."
	]

	for l in lines:
		say(l)

	# stop blinking the lights
	#
	lightThread.blinkOff()


def sayButtonInstructions():
	lines = [
		"Great. Thank you "+childsName+".",
		"Now I'll tell you what the buttons do.",
		"When you press the black button, I'll tell you what time it is.",
		"When you press the red button, I'll play a song for you.",
		"If you want the song to stop, press the red button again."
	]

	for l in lines:
		say(l)

def sayFinalInstructions():
	lines = [
		"OK "+childsName+".",
		"That's all for now.",
		"Thank you for listening.",
		"You can press the red or black button now."
	]

	for l in lines:
		say(l)
