import calendar

m, d, y = map(int, input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
# print (datetime(y, m, d).strftime("%A").upper())
