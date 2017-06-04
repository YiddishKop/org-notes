# 当两个进程使用 shared memory 进行IPC的时候
# 很容易出现由于读取 shared memory 的顺序和时间不同
# 造成数据误处理问题：
# 这时根据 samephore 机制，需要给进程加上信号，当信号量=1
# samephore = 1 -> lock
# 1. main process create a lock
# 2. sub process must *acquire* this lock before access shared memory
# 3. sub process must *release* this lock after leaving shared memory
# 4. function who want w/r shared memo in main process must add actions of *acquire* and *release* of this lock
# 5. main process can have manyh locks to control access to many shared memory variables

import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target = deposit, args=(balance, lock))
    w = multiprocessing.Process(target = withdraw, args=(balance, lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
