#!/bin/python3

import sys

# input e.g. 07:05:45PM
timestr = input().strip()
pm = (timestr[8:10] == "PM")
if pm:
	hours = int(timestr[0:2]) + 12
	res = str(hours).zfill(2) + str(timestr[2:8])
	print(res)
else:
	print(timestr[0:8])
