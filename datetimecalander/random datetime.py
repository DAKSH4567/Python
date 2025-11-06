import random
from datetime import datetime, timedelta


start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 12, 31)

time_between = end_date - start_date
seconds_between = time_between.total_seconds()

random_seconds = random.randint(0, int(seconds_between))
random_date = start_date + timedelta(seconds=random_seconds)
print("random date and time:", random_date)