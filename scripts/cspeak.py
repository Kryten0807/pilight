# speak a phrase, caching the audio (MP3) file for later access
#

import argparse
import hashlib
import os
import subprocess
import urllib

# the cache folder
#
cacheFolder = './storage/'

# get the script arguments
#
parser = argparse.ArgumentParser(description="Render an English text string as an MP3 file using Google's text to speech engine.")
parser.add_argument('words', nargs='+')

args = parser.parse_args()

# build the sentence from the list of words
#
sentence = " ".join(args.words)

# get the output file name
#
output = cacheFolder + hashlib.md5(sentence).hexdigest() + '.mp3'

# does the file exist? if not, retrieve it
#
if( not os.path.exists(output) ):
	# build the list representing the arguments for google
	#
	urlargs = {
		'ie': 'UTF-8',
		'tl': 'en',
		'q': sentence
	}

	# call the shell command to get the mp3 file
	#
	subprocess.call([
		'wget',
		'-q',
		'-U',
		'Mozilla',
		'-O',
		output,
		'http://translate.google.com/translate_tts?'+urllib.urlencode(urlargs)
	])

# play the sound
#
subprocess.call([
	'mpg123',
	'-q',
	output
]);
