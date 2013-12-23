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



