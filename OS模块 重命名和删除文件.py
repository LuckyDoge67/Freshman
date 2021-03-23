"""

file ：OS模块 重命名和删除文件.py
date :2021.03.21
author :Lucky
desc :

"""

# 创建一个test1.txt文件
f = open("test1.txt", "w")
# 当不需要该语句时在上面语句前加#

# 下面的语句请在不需要的语句前加#
import os

# 重命名文件test1.txt到test2.txt
os.rename("test1.txt", "test2.txt")

# 删除文件test2.txt
os.remove("test2.txt")
