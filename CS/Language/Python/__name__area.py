# if __name__ == '__main__':
# 这条语句相当于python程序的 entry point
# entry point is where execution begins
# entry point of C is ''void main()'
# entry point of Java is 'public static void main(String[] args)'

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

def calculate_area(base, height):
    # __name__ 从本程序执行，那么就是 __main__
    # 从其他程序import后执行，就是文件名
    print("__name__: ", __name__)
    return 1/2*(base*height)

if __name__ == '__main__':
    print("I am in area.py")
    a = calculate_area(10, 20)
    print("area: ", a)
