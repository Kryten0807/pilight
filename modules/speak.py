# speak.py
#
# speech related functions

from subprocess import call

# say a line of text
#
def say(text):
	# say the text
	#
	call([ "./scripts/speak", text ])


def sayIntroduction():
	text = [
		"Hello "+childsName,
		"I'm your new talking clock.",
		"Would you like me to tell you how I work?",
		"Press the red button or the black button."
	]

	for t in text:
		say(t)


