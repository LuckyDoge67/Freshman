"""

file ：位运算符.py
date :2021.03.20
author :Lucky
desc :

"""
a = 60                   # 60 = 0011 1100
b = 13                   # 13 = 0000 1101
c = 0                    # 0  = 0000 0000

# &，与运算符，同1为1，否则为0
c = a & b
print('1 - c的值为：', c)
print('1 - c的二进制为：', bin(c))
# |，或运算符，只要有一个1便为1，否则为0
c = a | b
print('2 - c的值为：', c)
print('2 - c的二进制为：', bin(c))
# ^,异或运算符，相异为1，否则为0
c = a ^ b
print('3 - c的值为：', c)
print('3 - c的二进制为：', bin(c))
# ~，取反运算符
c1 = ~a
c2 = ~b
print('4 - c1的值为：', c1)
print('4 - c1的二进制为：', bin(c1))
print('4 - c2的值为：', c2)
print('4 - c2的二进制为：', bin(c2))
# <<，左移运算符，右边的数字表示移动的位数，高位丢弃，低位补零
c = a << 3
print('5 - c的值为：', c)
print('5 - c的二进制为：', bin(c))
# >>，右运算符，右边的数字表示移动的位数，低位丢弃，高位补零
c = a >> 3
print('6 - c的值为：', c)
print('6 - c的二进制为：', bin(c))
