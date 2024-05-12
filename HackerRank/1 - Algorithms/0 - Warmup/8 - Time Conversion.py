# input e.g. 07:05:45PM
time_string = input().strip()
is_pm = (time_string[8:10] == "PM")
if is_pm:
	hours = int(time_string[0:2])
	if hours != 12:
		hours += 12
	res = format(hours, "02") + time_string[2:8]
	print(res)
# then am...
elif time_string[0:2] == "12":
	print("00" + time_string[2:8])
else:
	print(time_string[0:8])
