"""

file ：List与Tuple区别.py
date :2021.03.20
author :Lucky
desc :

"""
tuple1 = ('runoob', 786, 2.23, 'John', 70.2)
tinytuple = (123, 'John')
List = [786, 'John']

# tuple1[1] = 1000 # 元组中是非法应用
List[1] = 1000     # 列表中是合法应用

print(List)
print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tinytuple * 2)
print(tuple1 + tinytuple)
