fruits = '苹果5个，香梨4个，西瓜3个，哈密瓜6个，桃子3个，桔子7个'
for i in fruits:
    if i == '个':
        Num = int(fruits[int(i)-1])
        print(Num)
