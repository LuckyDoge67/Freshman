# _*_coding=utf-8 _*_
"""

file ：if-03-elif.py
date :2021.03.17
author :Lucky
desc :

"""
holiday_name = input("今天是是什么日子：")
if holiday_name == '情人节':
    print("买玫瑰，看电影")
elif holiday_name == '100天纪念日':
    print("买口红，吃大餐")
elif holiday_name == '生日':
    print("买蛋糕，送全套口红")
else:
    print("有你的每一天都是情人节")
