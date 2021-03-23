"""

file ：File对象的属性.py
date :2021.03.21
author :Lucky
desc :

"""

# 打开一个文件(若没有该文件，会创建一个新的)
fo = open("foo.txt", "w")
print("文件名:", fo.name)
print("是否已关闭:", fo.closed)
print("访问模式:", fo.mode)

# 关闭一个文件
fo.close()
print("是否已关闭:", fo.closed)


# write()方法
# 打开一个文件
fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery godd site\n")

# 关闭打开的文件
fo.close()


# read()方法
# 打开一个文件
fo = open("foo.txt", "r")
str1 = fo.read(10)
print("读取的字符串是:", str1)

# 关闭一个文件
fo.close()


# 文件定位( tell(), seek(offset, from) )
# 打开一个文件
fo = open("foo.txt", "r+")
str2 = fo.read(10)
print("读取的字符串是:", str2)

# 查找当前位置
position = fo.tell()
print("当前文件位置", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str2 = fo.read(10)
print("重新读取字符串:", str2)

# 关闭打开的文件
fo.close()
