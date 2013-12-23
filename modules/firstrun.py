# firstrun.py
#
# functions  related to the "first run" functionality

# is this the first run of the application?
#
def isFirstRun():
	return not os.path.exists('storage/firstRun')

# set the "first run" flag
#
def setFirstRunFlag():
	# write something into the file
	#
	with open('storage/firstRun', 'w') as f:
		f.write('')
