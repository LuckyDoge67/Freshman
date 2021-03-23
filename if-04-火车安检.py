# _*_coding=utf-8 _*_
"""

file ：if-04-火车安检.py
date :2021.03.17
author :Lucky
desc :

需求:
1.定义布尔型变量 has_ticket 表示是否有车票
2.定义整型变量 knife_length 表示刀的长度
3.首先检查是否有车票,如果有,才允许进行安检
4.安检时,需要检查刀的长度,判断是否超过 10cm
如果超过 10cm,提示刀的长度,不允许上车
如果不超过 10cm,安检通过
5.如果没有车票,不允许进门

"""
has_ticket = True
if has_ticket:
    print("车票检测通过，请先进行安检")
    knife_length = int(input("刀的长度："))
    if knife_length > 10:
        print("长度%d超过限定长度，安检不通过，不允许上车" % knife_length)
    else:
        print("长度%d未超过限定长度，安检通过，可以上车" % knife_length)
else:
    print("未购买车票，不允许上车")
