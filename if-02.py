# _*_coding=utf-8 _*_
"""

file ：if-02.py
date :2021.03.17
author :Lucky
desc :

"""
# 1.定义一个整数变量，要求年龄在0~120之间
age = int(input("\033[1;38m 请输入您的年龄："))
if 0 <= age and age <= 120:  # 这里原来是age>=0 and age<=120
    print("\033[1;32m 年龄符合要求")
else:
    print("\033[1;31m 年龄不符合要求")

# 2.定义两个整数变量 python_score,c_score,编写代码判断成绩是否合格
python_score = int(input("\033[1;38m 请输入python的成绩："))
c_score = int(input("\033[1;38m 请输入c语言的成绩："))
if python_score >= 60 or c_score >= 60:
    print("\033[1;32m 成绩合格")
else:
    print("\033[1;31m 成绩不合格")

# 3.定义一个布尔型变量 is_employee,编写代码判断是否是本公司员工,如果不是提示不允许入内
is_employee = False
if is_employee:
    print("\033[1;32m 是本公司的员工，允许进入公司")
else:
    print("\033[1;31m 非公司员工，禁止入内")
