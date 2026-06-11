from datetime import datetime, timedelta

now = datetime.now()
future = now + timedelta(7)
past = now - timedelta(0, 0, 0, 0, 65, 0, 0)
print(now, future, past)

string_time = now.strftime("%Y_%d_%m, %H,%M,%S")
print(string_time)
parsed_time = datetime.strptime("2026,06,05", "%Y,%m,%d")