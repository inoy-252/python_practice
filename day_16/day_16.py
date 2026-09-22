from datetime import datetime, timedelta

now = datetime.now()
print("Year:     ", now.year)
print("Month:    ", now.month)
print("Day:      ", now.day)
print("Hour:     ", now.hour)
print("Minute:   ", now.minute)
print("Timestamp:", now.timestamp())

print(now.strftime("%m/%d/%Y, %H:%M:%S"))
print(now.strftime("%d %B %Y"))

date_string = "16 April, 2004"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Parsed Object:", date_object)
print("Extracted Year:", date_object.year)
print("Extracted Month:", date_object.month)
print("Extracted Day:", date_object.day)


new_year = datetime(2027, 1, 1)
time_left = new_year - now

print("Days left until New Year:", time_left.days)

life_span = now - date_object
print("you have been alive for", life_span.days, "days")

future_date = now + timedelta(days=45)
print("45 days from today will be ", future_date.strftime("%d/%B/%Y"))
