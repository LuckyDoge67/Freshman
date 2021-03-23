# _*_coding=utf-8 _*_
"""

file ：for-02 计数.py
date :2021.03.17
author :Lucky
desc :

需求1：
fruits='苹果5个，香梨4个，西瓜3个，哈密瓜6个，桃子3个，桔子7个'
使用for循环统计水果的总数
"""

# 用标号的方法简单
Sum = 0
fruits = '苹果5个，香梨4个，西瓜3个，哈密瓜6个，桃子3个，桔子7个'
for i in range(len(fruits)):
    if fruits[i] == '个':
        Num = int(fruits[i-1])
        Sum = Sum + Num
print('Sum=', Sum)

# 用列表似乎不行，或者说会比较麻烦
Sum2 = 0
i = 0
fruits2 = ['苹''果''5''个''，''香''梨''4''个''，''西''瓜''3''个''，''哈''密''瓜''6''个'''
           '，''桃''子''3''个''，''桔''子''7''个']
if i <= 29:
    if fruits2[i] == '个':
        Num2 = int(fruits2[i-1])
        Sum2 = Sum2 + Num2
        i = i+1
    else:
        i = i+1
else:
    print('Sum2=', Sum2)
