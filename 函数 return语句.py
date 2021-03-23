"""

file ：函数 return语句.py
date :2021.03.21
author :Lucky
desc :

"""


# 可写函数说明
def sum1(arg1, arg2):
    """返回2个参数的和"""
    total1 = arg1 + arg2
    print("函数内:", total1)
    return total1


# 调用sum1函数
total = sum1(10, 20)
