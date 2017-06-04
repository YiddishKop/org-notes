# 这个程序的运行结果比较有意思，
# 他最后会返回
# square 4
# result [4]
# square 9
# result [4, 9]
# square 64
# result [4, 9, 64]
# square 81
# result [4, 9, 64, 81]
# result []
# Done!
# 为什么会多出一个 result []
# Every process has its own address space(virtual memory)
# Thus program variables are not shared between two process
# You need to use interprocess conmmunication(IPC) tech if
# you want to share data between two process
# 虽然声明了全局变量，但是他的作用范围也是自己的地址空间(virtual memory)
# 所以这里全局变量是没用的，需要一种跨进程通信机制：IPC
# IPC 进程间通信的方式有三种：
# 1. File
# 2. Shared memory
# 3. Message pipe
# 前面讲过的，multiprocessing.Array/Value/Queue 都属于第二种 shared memory

# 对比 Multiprocess Queu        and       Queue Module
# ------------------------------|------------------------------
# import multiprocessing        |     import queue
# q = multiprocessing.Queu()    |     q = queue.Queue()
#                               |
# * lives in shared memory      |     * lives in in-process memory
# * Used to shared data between |     * Used to share data between
#   processes                   |       threads

import time
import multiprocessing

def calc_square(numbers, q):
    # Queue is a FIFO data structure.
    # has API: put(), get()
    for n in numbers:
        q.put(n*n)

if __name__ == '__main__':
    arr = [2,3,8,9]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=calc_square, args=(arr, q))
    p1.start()
    p1.join()

    while not q.empty():
        print(q.get())
