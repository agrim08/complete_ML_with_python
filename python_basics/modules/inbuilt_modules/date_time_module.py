from datetime import datetime,timedelta
now = datetime.now()
print(now)

yesterday = now - timedelta(days= 1) #tell me the time 1 day ago
print(yesterday)