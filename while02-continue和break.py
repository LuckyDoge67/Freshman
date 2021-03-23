"""

file ：while02-continue和break.py
date :2021.03.21
author :Lucky
desc :

"""

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非偶数时跳过该次循环，进入下一次循环
        continue
    print()  # 输出偶数

a = 1
while 1:  # 循环条件为1必定成立
    print(a)  # 输出1~10
    a += 1
    if a > 10:  # 当a大于10时，跳出全部循环
        break
i