import time

wait_time = 1
max_retries = 6
attempt = 0

while attempt < max_retries:
    print("Attempts", attempt +1 ,"waitTime",wait_time)
    time.sleep(wait_time)
    wait_time = wait_time *2
    attempt = attempt +1
