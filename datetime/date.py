import time;

# ticks = time.time();
# print(ticks);

# print(time.localtime())

# cal = time.localtime();

# astime = time.asctime(cal(time.time()));

# print(astime);

# localtime = time.asctime();

# getting calendar for a month.
import calendar;

cal = calendar.month(2022,3)
print(cal);


# Time module 
# 1: time.altzone

# time altzone() method:
# the time module is the attribute of the time module.
# this return the offset of the local dst time zone,in seconds west of UTC ,if one is defined. this is negative 
# if the local DST timezone is east of UTC (as in western Europe,including the UK). only use this if daylight is nonzero.

# syntax
# time.altzone

print(time.altzone)

# 2: Time asctime() method.

# Time asctime() converts a tuple or struct_time representing a time as returned by 
# gmtime() or localtime() to a 24-character string of the following form: 

# syntax: time.asctime((t))

# t = time.localtime()
localtime = time.asctime()
print(localtime)