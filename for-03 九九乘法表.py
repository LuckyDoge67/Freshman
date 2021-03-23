# _*_coding=utf-8 _*_
"""

file ：for-03 九九乘法表.py
date :2021.03.17
author :Lucky
desc :

"""


def print99():                                       # 定义函数print99
    for i in range(1, 10):                           # i为从1~10取值
        for j in range(1, i + 1):                    # 当i取值时，j为从1~i+1取值
            print('%d * %d = %2s ' % (j, i, i * j))  # 打印j*i的乘法
        print('\n')                                  # 循环结束换行


class PrintTable(object):                            # 定义一个类
    """打印九九乘法表"""

    def __init__(self):
        print('开始打印九九乘法表')
        print99()


if __name__ == '__main__':
    pt = PrintTable()
