import datetime

now = datetime.datetime.now()
print('Current date & time: ',now)
print('Current date Only: ',datetime.date.today())

d=datetime.date(2023,12,25)
print('Specific Date: ',d)
t=datetime.time(14,30,15)
print(t)

print('Year: ',now.year)
print('Month: ',now.month)
print('day: ',now.day)
print('Hour: ',now.hour)
print('Minute: ',now.minute)

# formate Date (strftime)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
# %Y -> YEAR
# %m -> Month
# %d -> Day
# %H -> Hour
# %M -> minute
# %S -> Seconds

## Parse
date_str = "2025-05-03"
date_obj = datetime.datetime.strptime(date_str,"%Y-%m-%d")
print(date_obj)