"""

file ：成员运算符.py
date :2021.03.20
author :Lucky
desc :

"""

a = 10
b = 20
List = [1, 2, 3, 4, 5]

# 判断变量a是否在List中
if a in List:
    print("变量a在给定的列表List中")
else:
    print("变量a不在给定的列表List中")
# 判断变量b是否在List中
if b not in List:
    print("变量b不在给定的列表List中")
else:
    print("变量b在给定的列表List中")

# 修改变量a的值
# 判断修改后变量a是否在List中
a = 2
if a in List:
    print("修改后变量a在给定的列表List中")
else:
    print("修改后变量a不在给定的列表List中")
