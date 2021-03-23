"""

file ：函数 参数.py
date :2021.03.21
author :Lucky
desc :

"""


# 关键字参数顺序
# 可写函数说明
def printinfo1(name, age):
    """打印任何传入的字符串"""
    print("Name:", name)
    print("Age", age)
    return


# 调用printinfo1函数
printinfo1(age=50, name='Niki')


# 默认参数
# 可写函数说明
def printinfo2(name, age=35):
    """打印任何传入的字符串"""
    print("Name:", name)
    print("Age", age)
    return


# 调用printinfo2函数
printinfo2(age=50, name='Niki')
printinfo2(name='Niki')


# 不定长参数
# 可写函数说明
def printinfo3(arg1, *vartuple):
    """打印任何传入的字符串"""
    print("输出:")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo3函数
printinfo3(10)
printinfo3(70, 60, 50)


# 匿名函数（用lambda表达式创建）
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2


# 调用sum函数
print("相加后的值为:", sum(10, 20))
print("相加后的值为:", sum(20, 20))
