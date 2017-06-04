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
import time
import multiprocessing

square_result = []

def calc_square(numbers):
    # 这里的global基本失效，每一个进程都会有各自的一个
    # square_result
    global square_result
    for n in numbers:
        # time.sleep(5)
        print('square ' + str(n*n))
        square_result.append(n*n)
        print('result ' + str(square_result))

    print('with in a process: result ' + str(square_result))

if __name__ == '__main__':
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()

    # 这里打印的是原始进程的 square_result
    print('result ' + str(square_result))
    print("Done!")
