import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

import datetime
x = datetime.datetime.now()

print(x.year)

from datetime import date


today = date.today()


print(f"Today's date: {today}")


from datetime import date

today = date.today()

print(f"Present Year:{today.year}")
print(f"Present Month:{today.month}")
print(f"Present Date:{today.day}")