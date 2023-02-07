# Timer-Application
The Timer Application is a simple program built using the Python programming language.

Introduction:

The Timer Application is a simple program built using the Python programming language. The purpose of this application is to provide users with a timer that they can use to keep track of the time spent on a task. The program takes in the number of seconds the user wants the timer to run for, and then displays a message once the timer is finished.

Technologies Used:
- Python 3.11.1

Key Parts of the Code:

- timer_duration = int(input()): This line of code takes in the number of seconds the user wants the timer to run for.
- time.sleep(timer_duration): This line of code starts the timer and the timer will run for the number of seconds specified by the user.
- print("Time's up!"): This line of code displays the message "Time's up!" once the timer finishes.

Design Decisions:

In designing the Timer Application, I chose to use the time module in Python to implement the timer. The time module provides a simple and easy-to-use method for adding a delay (i.e. the timer) to a program. I also decided to use a simple print statement to display the message "Time's up!" once the timer finishes, as this was the easiest way to inform the user that the timer has finished.

Reflection:

Working on the Timer Application was a great opportunity to further my understanding of the time module in Python. I also learned how to take user input and use it to determine the length of a timer. One challenge I faced was figuring out how to handle user input effectively. However, I was able to overcome this challenge by using the int function to convert the user input into a numerical value that could be used to specify the length of the timer.

Additional Resources:
- Python documentation for the time module: https://docs.python.org/3/library/time.html
