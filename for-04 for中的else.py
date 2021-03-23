"""

file ：for-04 for中的else.py
date :2021.03.20
author :Lucky
desc :

"""

# 判断10~20中的数哪些是质数，将不是质数的数用乘法表示出来
for num in range(10, 20):  # 迭代10~20之间的数字
    for i in range(2, num):  # 根据因子迭代，若不可以除以（2~它本身-1）的其中任意一个数，则为质数
        if num % i == 0:     # 确定第一个因子
            j = num / i      # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break            # 跳出当前for循环（第二个for语句）若将这行去掉，则可以得到非质数的数每个乘法因子
    else:                    # 第一个for循环的else部分
        print(num, '是一个质数')
