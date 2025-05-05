from datetime import datetime

dt= datetime(2023,12,25,0,0,0)

#Convert to epoch
epoch_time = int(dt.timestamp())
print(epoch_time)

dt1 = datetime.fromtimestamp(1703442600)
print(dt1)