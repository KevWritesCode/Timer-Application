import time

def timer():
    print("Welcome to the Timer App")
    print("Enter the number of seconds you would like the timer to run for:")
    timer_duration = int(input())

    print("Starting timer...")
    time.sleep(timer_duration)
    print("Time's up!")

timer()
