# speak.py
#
# speech related functions

from subprocess import call

def say(text):
	# say the text
	#
	call([ "./scripts/speak", text ])