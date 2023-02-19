# Python date

#1. Write a Python program to subtract five days from current date.

from datetime import date, timedelta
dt = date.today() - timedelta(5)

print("Current Date:", date.today())
print("5 days before Current Date:", dt)
#x = datetime.datetime.now()
#y = datetime.datetime(x.year, x.month, x.day - 5)
#print(y)

#2. Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta
dt = date.today() + timedelta(1)
dy = date.today() - timedelta(1)
print("Yesterday was ", dy)
print("Today is ", date.today())
print("Tomorrow will be ", dt)
#3. Write a Python program to drop microseconds from datetime.

import datetime
dt = datetime.datetime.today().replace(microsecond=0)

print(dt)

#4. Write a Python program to calculate two date difference in seconds.

from datetime import datetime, time
def difference(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2023-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print(str(difference(date2, date1)) + " seconds")
print()