import datetime
from datetime import timedelta

today=datetime.date.today()
yesterday=today-timedelta(1)
tomorrow=today+timedelta(1)

print('Today:', today)
print('Yesterday:', yesterday)
print('Tomorrow:', tomorrow)