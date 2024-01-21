# datetime zone, operations between datetime objects -- how many days, seconds have passed

# the time factor

import datetime

mytime = datetime.time(13, 40, 20, 10) # (hour, minutes, seconds, microseconds)

print(mytime.minute)

print(mytime.hour)

print(mytime) # 13:40:20.000010

print(mytime.microsecond) # 10

# microseconds used in scientific settings

print(type(mytime)) # <class 'datetime.time'> -- it has no date associated with this

today = datetime.date.today() # date(year, month, date)

print(today) # 2024-01-21

print(today.year) # print attributes


print(today.ctime()) # Sun Jan 21 00:00:00 2024
# some databases store time in this format -- it might be useful

# DATE AND TIME ALTOGETHER
from datetime import datetime

mydatetime = datetime(2023, 1, 21, 17, 30, 20)

print(mydatetime, '\n') # 2023-01-21 17:30:20
# largest time scale --> smallest

# update mydatetime because it doesn't happen in place
# method call to change current date/time
mydatetime = mydatetime.replace(year = 2024) # 2024-01-21 17:30:20
print(mydatetime, '\n')



# SIMPLE ARITHMETIC COMMON WITH DATETIME OBJECTS
# for eg. how much time sb logged in your website on a certain day
# and logged back out on another day/certain date time
# how long they spent on the website/logged in


# DATE

from datetime import date

date1 = date(2024, 1, 12)
date2 = date(2023, 11, 3)

result = date1 - date2

print(result) # 70 days, 0:00:00
print(type(result)) # <class 'datetime.timedelta'>

# there may be issues with leap years in case of long distances between years 

print(result.days)


# DATETIME 

datetime1 = datetime(2024, 1, 10, 22, 0)
datetime2 = datetime(2023, 11, 3, 12, 0)

result = datetime1 - datetime2
print(result) # 68 days, 10:00:00

print(result.seconds) # 36000

# everything reported as seconds -- days + hours + ..
print(result.total_seconds()) # 5911200.0
