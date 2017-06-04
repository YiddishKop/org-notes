from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1 = time.time()
    p = Pool()
    # Map_reduce 模型，
    # map负责分发数据给不同的 cpu-core
    # fn 负责在各自的 cpu-core 中运算
    # reduce 负责组合最终数据
    # map(<fn-to-item>, <dataset-to-map>)
    # map 这个函数同时具有 map 和 reduce 的双重功能
    result = p.map(f, range(1000000))
    p.close()
    p.join()
    print("Pool took: ", time.time() - t1)

    t2 = time.time()
    result = []
    for x in range(1000000):
        result.append(f(x))

    print("Serial processing took: ", time.time() - t2)
