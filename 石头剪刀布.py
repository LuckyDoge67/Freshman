# _*_coding=utf-8 _*_
"""

file ：石头剪刀布.py
date :2021.03.17
author :Lucky
desc :

需求:
1.从控制台输入要出的拳 —布：1,剪刀：2,石头：3
2.电脑随即出拳–先假定电脑只会出剪刀,完成整体代码功能
3.比较胜负
石头 胜 剪刀
剪刀 胜 布
布 胜 石头

"""
import random as rm
import sys

com_1 = rm.randint(1, 3)
peo = int(input("请输入您要出的拳(输入1代表“石头”；2代表“剪刀”；3代表“布”)："))
# 1.扫描输入的数字是否正确
if peo < 1 or peo > 3:
    print("\033[1;31m 请输入正确的数字")
    sys.exit()
else:
    # 2.扫描电脑出什么拳
    if com_1 == 1:
        print("电脑出的是石头")
    elif com_1 == 2:
        print("电脑出的是剪刀")
    elif com_1 == 3:
        print("电脑出的是布")
    # 3.判断输赢
    if (com_1 == 1 and peo == 3) or (com_1 == 2 and peo == 1) or (com_1 == 3 and peo == 2):
        print("你赢了！")
    elif (com_1 == 1 and peo == 1) or (com_1 == 2 and peo == 2) or (com_1 == 3 and peo == 3):
        print("平局！")
    elif (com_1 == 1 and peo == 2) or (com_1 == 2 and peo == 3) or (com_1 == 3 and peo == 1):
        print("你输了！")
