import datetime

d1=datetime.datetime(2023,2,24)
d2=datetime.datetime(2023,1,10)
ans=d1-d2

print(ans.total_seconds(), 'seconds')
