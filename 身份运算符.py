"""

file ：身份运算符.py
date :2021.03.20
author :Lucky
desc :

"""

a = 20
b = 20
print(id(a))
print(id(b))
if a is b:
    print('a和b有相同的标识')
else:
    print('a和b没有相同的标识')

if a is not b:
    print('a和b没有相同的标识')
else:
    print('a和b有相同的标识')

# 修改变量b的值
b = 30
print(id(a))
print(id(b))
if a is b:
    print('修改后a和b有相同的标识')
else:
    print('修改后a和b没有相同的标识')

if a is not b:
    print('修改后a和b没有相同的标识')
else:
    print('修改后a和b有相同的标识')

# is 与 == 的区别
''' 

is 与 == 的区别:
b=a将两者指向同一个对象
而b=a[:]会创建一个新的与a完全相同的对象，但是与a并不指向同一对象。
在计算机中，不同的对象即不同的内存地址。
可理解为：b=a将创建a与b两个快捷方式并指向同一文件；
而b=a[:]先将a指向的文件复制一份作为副本，然后创建一个指向该副本的快捷方式b。
二者不同表现为当两者指向同一对象时，改变其中任意一个，都会改变对象的值，也就是同时改变a，b的值。

'''
a = [1, 2, 3]
b = a
print(b, id(a), id(b))
print(b is a)
print(b == a)
b = a[:]
print(b, id(a), id(b))
print(b is a)
print(b == a)
