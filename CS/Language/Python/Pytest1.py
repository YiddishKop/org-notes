# Python testing frameworks
# 1. unittest
# 2. nose
# 3. pytest

# 使用 pytest 有两个要求：
# 1. test 中的函数名字必须是 'test_<func name>'
# 2. test 文件名字必须是'test_<.py file name>

# pytest 常用命令
# $ py.test -v
# this will give the specification of every func

# @pytest.mark.skip(reason = "I dont need test this fn")
# 把这条语句放在test函数上方，表示测试时自动忽略

# import pytest
# @pytest.mark.skipif(sys.version_info < (3,5), reason = "I dont need test this fn")
# 必须 import pytest 之后才能使用 decorator
# 可以根据条件来确定是否skip：skipif

# $ pytest -v -rxs
# 这个命令会给出skip的理由

# 选择测试哪些函数： -k -> keyword, -m -> mark
# $ pytest -k multiply
# 选择要test的关健词，函数名中包含这些关键字才会被测试

# $ pytest -m <somename>
# 这条语句是只测试那些 被decorator(@pytest.mark.<somename>)标记为某个
# <somename> 名字的函数

# $ pytest -m "not <somename>"
# 这条语句是只测试那些非<somename>mark的函数

def calc_total(a, b):
    return a+b

def calc_multiply(a, b):
    return a*b
