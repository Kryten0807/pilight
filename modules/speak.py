# speak.py
#
# speech related functions

from subprocess import call
from time import localtime, strftime


# say a line of text
#
def say(text):
	# say the text
	#
	call([ "./scripts/speak", text ])

def sayGreeting():
	# say the greeting
	# @todo make this more fun - personalized, based on time of day, etc.
	#
	say("Hello, "+childsName+".")
	say("What would you like to do?")

def sayCurrentTime():
	# get the current time
	# @todo convert from 24 hr clock to 12 hr
	#
	t = strftime("%H:%M", localtime())

	# say it
	#
	say("It is now "+t+".")

	# add the state of the lights (ie. not time to get up yet)
	state = checkLights()

	if( state=='green' ):
		say("It's time to get up.")
	elif( state=='yellow' ):
		say("It's almost time to get up, but not yet.")
	else:
		say("It's not time to get up.")


def sayIntroduction():
	text = [
		"Hello "+childsName,
		"I'm your new talking clock.",
		"Would you like me to tell you how I work?",
		"Press the red button or the black button."
	]

	for t in text:
		say(t)


def sayLightInstructions():
	text = [
		"Great. Thank you, "+childsName,
		"Look at the front of my box. You'll see three big round lights.",
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
		"Thanks for listening, "+childsName,
		"Press a button and I'll tell you more."
	]

	for t in text:
		say(t)

def sayButtonInstructions():
	text = [
		"Great. Thank you, "+childsName,
		"Now I'll tell you what the buttons do.",
		"When you press the black button, I'll tell you what time it is.",
		"When you press the red button, I'll surprise you with something fun.",
		"Try the red button now!"
	]

	for t in text:
		say(t)
