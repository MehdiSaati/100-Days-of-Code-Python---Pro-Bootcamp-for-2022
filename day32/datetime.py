import datetime as dt

now = dt.datetime.now()
print(now)

year = now.year
print(year)

month = now.month
print(month)

day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year= 1989, month=12, day=10, hour=6)
print(date_of_birth)
