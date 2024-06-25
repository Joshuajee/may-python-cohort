import datetime

past_date = datetime.datetime(2022, 6, 17)

current_date = datetime.datetime.now()

print(current_date)

print(current_date.year)

print(current_date.timestamp())

print(current_date)


print(past_date)

print(datetime.timedelta(days=current_date.day, hours=current_date.hour))

