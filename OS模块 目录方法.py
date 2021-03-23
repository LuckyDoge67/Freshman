"""

file ：OS模块 目录方法.py
date :2021.03.21
author :Lucky
desc :

"""

# 在当前目录下创建一个新目录
import os

# mkdir()创建目录test
# 创建目录test
# os.mkdir("test")

# chdir()改变当前的目录
# 将当前目录改为”/home/newdir“
# os.chdir("/home/newdir")

# getcwd()显示当前的工作目录
# 给出当前的目录
print(os.getcwd())

# rmdir()删除目录，目录名称以参数传递
# 在删除这个目录之前，它的所有内容应该先被清除
# 删除"/tmp/test"目录
# os.rmdir("/tmp/test")
