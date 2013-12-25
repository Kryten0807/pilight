# time.py
#
# Some time related functions

import datetime
import time

def getLocalTime():
	return datetime.time(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)