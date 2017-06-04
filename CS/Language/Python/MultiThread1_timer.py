# MultiThreading - 1
# What is Multithreading?
# Threads can be thought of as separate programs running along side each other.
# However they run within one process, meaning they can share data between one another easier than actual separate programs.

# What is Multithreading?
# The challenge of Threads is that they can be hard to manage. Especially when a piece of data is being used by more than one thread.
# Threads can be used just for quick tasks like calculating a result from an algorithm or for running slow processes in the background while the program continues.
# What is Multithreading?
# We can also create many threads to try and find an answer faster. Perhaps we need to hash 100 passwords with md5. we could have 5-10 threads each hashing a password making the total time 5-10 times faster!


# How it works!
# We already use one thread in our programs. The Main thread.
# When we create a new thread it runs along side our main thread.
# On Windows it’s easy to open your task manager and see how many threads programs are using.

# timer Program
# A basic timer program essentially hello world for threading.
# Each timer thread will output the current time
# Then wait a certain time before outputting again.

from threading import Thread

import time

def timer(name, delay, repeat):
    print("Timer: " + name + "Started")
    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer: " + name + " Completed")

def Main():
    t1 = Thread(target = timer, args = ("Timer1", 1, 5))
    t2 = Thread(target = timer, args = ("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main Completed")

if __name__ == "__main__":
    Main()
