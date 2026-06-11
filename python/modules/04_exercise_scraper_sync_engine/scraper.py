import re
import datetime
raw_string = "Heads up! The next major round drops on 2026-06-15 14:30:00, followed by a blitz on 2026-06-18 09:00:00."
dates = list(re.findall(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}", raw_string))
print(dates)

converted_dates = []
time_diff = []
for date in dates:
    conv = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    converted_dates.append(conv)
    diff =  conv - datetime.datetime.now()
    time_diff.append(diff)
    hours = diff.seconds // 3600
    print(diff.days, diff.days, hours)
print(set(time_diff))


