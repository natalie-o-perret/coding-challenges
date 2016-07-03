#!/bin/python3

import sys

# input e.g. 07:05:45PM
timestr = input().strip()
pm = (timestr[8:10] == "PM")
if pm:
	hours = int(timestr[0:2])
	if hours != 12:
		hours += 12
	res = format(hours, "02") + timestr[2:8]
	print(res)
# then am...
elif timestr[0:2] == "12":
	print("00" + timestr[2:8] )
else:
	print(timestr[0:8])
