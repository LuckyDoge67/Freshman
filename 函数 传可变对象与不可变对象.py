"""

file ：函数 传可变对象与不可变对象.py
date :2021.03.17
author :Lucky
desc :

"""


# 传不可变对象
def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)


# 传可变对象
# 可写函数说明
def changeme(mylist):
    """修改传入的列表"""
    mylist.append([1, 2, 3, 4])
    print("函数内取值", mylist)


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值", mylist)
