# shareing Data Between process using Array and Value
import multiprocessing

def calc_square(numbers, result, v):
    v.value = 5.67
    # enumerate is useful for obtaining an indexed list:
    #     (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    number = [2, 3, 5]
    # shared memory variable
    # 'i' -> integer; 'd' -> double; '3' -> 3*item
    # 这个比 global 的范围更大，是进程间的
    result = multiprocessing.Array('i', 3)
    v = multiprocessing.Value('d', 0.0)
    p = multiprocessing.Process(target=calc_square, args=(number, result, v))
    p.start()
    p.join() # 子进程到这里就结束了

    print(result[:])
    print(v.value)
