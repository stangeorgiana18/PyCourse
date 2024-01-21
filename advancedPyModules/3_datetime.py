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

print(mydatetime.replace(year = 2024)) # 2024-01-21 17:30:20

