import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser()

    # 给程序添加副参数 add_mutually_exclusive_group
    # python argument.py 10 [-v/-q]
    # argparse.ArgumentParser().add_mutually_exclusive_group().xx
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")

    # 给程序添加参数
    # python argument.py 10
    # argparse.ArgumentParser().add_argument().xx
    parser.add_argument("num", help="The fibonacci number you wish to calculate.", type = int)
    parser.add_argument("-o", "--output", help = "Output result to a file,", action = "store_true")

    # 获取参数进行进一步处理
    # argparse.ArgumentParser().parse_args().[argument_name]
    args = parser.parse_args()
    result = fib(args.num)
    if args.verbose:
        print("the " + str(args.num) + "fib number is " + str(result))
    elif args.quite:
        print(result)
    else:
        print("Fib(" + str(args.num) + ") = " + str(result))
    if args.output:
        f  = open("fibonacci.txt", "a")
        f.write(str(result) + "\n")


if __name__ == '__main__':
    Main()
