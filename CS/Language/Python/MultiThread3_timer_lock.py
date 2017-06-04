# MultiThreading - 3
# Locks
# Locks can be a hard topic to grasp, well they were for me at least. The challenge with locks is knowing when to use one.
# We use a Lock to lock access to one thread.
# Because threads run simultaneously there is no guarantee that both threads wont try to use a variable at the same time.
# Modified Timer Program
# Similar to our previous timer program, however we will add a lock that will lock the thread currently printing the time.
# This program is mainly an example of what a Lock does.

# Semaphores
# Semaphores like locks restrict access to a thread.
# However semaphores can allow more than one lock to be acquired.
# You may have 10 threads running, but you only want 2 or 3 to have access to a piece of data at a time.

# When to use Threading
# Threading isn’t the answer to every problem.
# If your program logic has to run in a sequence, then threads wont help you out.
# If you are writing a GUI, then you want at least two threads. One for the GUI and one to do all the work in the background. To avoid the GUI being unresponsive.

# When to use Threading
# If the program is running on a CPU with only one core. Then there will be no performance improvement as the threads will be time split on the one core.
# It’s great for servers that deal with TCP connections to be multi-Threaded as you want to be able to handle more than 1 request at a time.

# 没加 lock 一段代码可以被多个 thread 同时执行
# 加上 lock 这断代码只能被一个 thread 执行，直到他释放锁，其他 thread 才能运行这段代码

import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: " + name + "Started")

    # add lock to this thread
    tLock.acquire()
    print(name + " Has acquire the lock")

    while repeat > 0:
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))
        repeat -= 1

    # release lock to this thread
    print(name + " is releasing the lock")
    tLock.release()

    print("Timer: " + name + " Completed")

def Main():
    t1 = threading.Thread(target = timer, args = ("Timer1", 1, 5))
    t2 = threading.Thread(target = timer, args = ("Timer2", 2, 5))
    t1.start()
    t2.start()

    print("Main Completed")

if __name__ == "__main__":
    Main()
