import math
from math import pi
import datetime 
from datetime import datetime, timedelta

# exercise 2.1
n = x = 1
print(n,x)

# exercise 2.2
r = 5
volume = 4/3 * pi * (r**3)
print(volume)

# exercise 2.2
"""Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
 $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
 60 copies?"""

cover_price = 24.95
discount = (1 - 0.40) * cover_price
print("discount per book is: ", discount)
total_numOfBooks = 60
total_costOfBooks = discount * total_numOfBooks
print(total_costOfBooks)
Shipping_cost = 3
additional_shipping = 0.75 * 59
total_shipping = Shipping_cost + additional_shipping
print(f'$ {total_costOfBooks + total_shipping}')

# exercise 2.2
"""If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
 tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
"""
start_time = datetime(2024, 1, 1, 6, 52, 0)
easy_pace = timedelta(minutes=8, seconds=15)
tempo_pace = timedelta(minutes=7, seconds=12)

total_runtime = easy_pace * 2 + tempo_pace * 3
eta = total_runtime + start_time
print(f"start time: {start_time.strftime('%I:%M:%S %p')}")
print(f"Total run time: {str(total_runtime)}")
print(f"Arrival time: {eta.strftime('%I:%M:%S %p')}")

