"""

file ：函数 全局变量和局部变量.py
date :2021.03.21
author :Lucky
desc :

"""

total = 0  # 在这里的total1是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    """返回2个参数的和"""
    total = arg1 + arg2  # 在这里的total1是局部变量
    print("函数内是局部变量:", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量:", total)
