"""

file ：while01.py
date :2021.03.21
author :Lucky
desc :

"""
# 输出整数
a = 1
odd = []
i = 0
while a < 10:
    if i <= 5:
        odd.append(a)
    a += 2
    i += 1
else:
    print(odd)

# 从列表中分别提取出奇数与偶数
numbers = [12, 37, 5, 42, 8, 3]  # 定义一个列表
even = []                        # 定义偶数列表
odd = []                         # 定义奇数列表
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(' 奇数为：', odd, '\n', '偶数为：', even)

# while中的else
count = 0
while count < 5:
    print(count, "is less than 5")
    count = count + 1
else:
    print(count, "is not less than 5")