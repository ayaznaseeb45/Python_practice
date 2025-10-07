# Write a Python program to implement an exponential backoff strategy that:

# Starts with a wait time of 1 second,

# Doubles the wait time after each retry,

# Stops after 5 retries.


import time
wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "Wait time:", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2  # double the wait time
    attempts += 1