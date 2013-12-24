# PiLight

A Raspberry Pi powered visual alarm.

Not sure what that means? Check out
[this page](http://www.tycen.com/2013/12/sleepi.html).

Like the gentleman who wrote the blog post above, I have a small child at home
who likes to get up ridiculously early on weekend mornings. Inspired by the post
above, and by the Raspberry Pi I had at home, I put together my own version.

## A Note about this Repository

This repository follows the "gitflow" system. All the development is being done
on the develop branch (and on feature branches where appropriate). When I'm
happy with the current state, changes will be merged into the master branch. As
of this writing (12/24/2013), neither the master branch nor the develop branch
are ready for use. I'll be doing some testing later today and will (hopefully)
merge the develop branch into the master branch in time for this to be deployed
as a Christmas present.

## What it Does

If you've read the post linked to above, you know that at it's heart this is a
red light/green light system to inform a small child (who can't tell time yet)
when it's acceptable to wake up mommy & daddy.

I wanted to add a little more to it, though - I wanted it to be fun! However,
it's now Dec. 23 and I want to sneak it into his room when he's asleep on
Christmas eve, so my first release of this script is going to be a little light
on options.


## A Note about this Repository

This repository follows the "gitflow" system. All the development is being done
on the develop branch (and on feature branches where appropriate). When I'm
happy with the current state, changes will be merged into the master branch. As
of this writing (12/24/2013), neither the master branch nor the develop branch
are ready for use. I'll be doing some testing later today and will (hopefully)
merge the develop branch into the master branch in time for this to be deployed
as a Christmas present.


## How it Works

The hardware on my system consists of three LEDs (red, yellow, and green) and
two push buttons (one red, one black). These are connected to the Pi via GPIO
pins. I have added audio output to the system, so I bought a tiny speaker which
is powered via USB and plugs into the Pi's audio jack.

Since I want my son to wake up with it on Christmas morning and start figuring
it out, I'm designing the script with two modes: a "first time" mode wherein
pushing either button results in a greeting and some simple instructions, and a
"normal operations" mode, where pushing one button states the time and pushing
the other does something else: it gives a simple weather report ("It's sunny!"
or "It's raining!" - weather reports provided by an online service), it plays
a song, it tells a joke, or it says something nice.

Here's some pseudocode describing the flow of the script:

	Loop:
		// Light the appropriate lights
		//
		checkLights()
		// Handle the buttons
		//
		if( checkButton(red) or checkButton(black) ):
			// when was the last button pressed? if more than two hours ago,
			// then say the appropriate greeting
			//
			if( lastButtonPress > 2 hours ago ):
				// is this the first run? if so, say the first run greeting and
				// the instructions
				//
				if( isFirstRun() ):
					sayIntroduction()
					sayInstructions()
					// set the first run flag
					//
					setFirstRunFlag()
				else:
					sayGreeting()
			else:
				// the child has been playing with it & has pressed a button
				// recently
				//
				if( checkButton(red) ):
					// the red button is pressed. Announce the time
					//
					sayCurrentTime()
				if( checkButton(black) ):
					// the black button is pressed. Do something fun
					//
					switch( rand() )
						case 1:
							sayWeather()
						case 2:
							sayJoke()
						case 3:
							playSong()
						case 4:
							sayNiceThing()
		# sleep a little while before starting the loop over
		sleep(delay)

Please note that this is the only python script I've written, apart from a
couple of copied & pasted scripts for the Pi. I'm sure I've violated some python
rules & customs. Please let me know if there are better ways to write this code!

## @TODOs and Enhancements

1. Add additional fun things to do: weather reports, jokes, etc.
1. Add a web interface to allow remote configuration by non-technical users
1. In the web interface, add a "say now" function to let users say things remotely