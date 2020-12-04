import random
rgmin=int(input('请输入随机数最小值：'))
rgmax=int(input('请输入随机数最大值：'))
if rgmax>=rgmin:
    rgd=random.randint(rgmin,rgmax) 
    pass
else:
    input('你是不是Der？')
    exit()
    pass
while True:
    inp=int(input('请猜从%s到%s的一个整数：'%(rgmin,rgmax)))
    if inp==rgd:
        input('猜对了')
        break
    elif inp >rgd:
        print('大了！')
        pass
    else:
        print('小了！')
        pass
