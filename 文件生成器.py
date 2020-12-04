import random
while True:
    inp=input('请输入想要生成的随机文件的大小（B/K/M/G/T）：')
    name=input('请输入想要生成的随机文件的名字（不得为空）：')
    Dan_wei=inp[-1]
    size=inp[:-1]
    if Dan_wei=='B':
        realsize=int(float(size))
        pass
    elif Dan_wei=='K':
        realsize=float(size)*1024
        pass
    elif Dan_wei=='M':
        realsize=float(size)*(1024*1024)
        pass
    elif Dan_wei=='G':
        realsize=float(size)*(1024*1024*1024)
        pass
    elif Dan_wei=='T':
        i=0
        while i==0:
            choice=input('Are you sure???(y/n)')
            if choice=='y':
                i=1
                realsize=float(size)*(1024*1024*1024*1024)
                pass
            pass
        pass
    else:
        print('输入有误')
        continue
    realsize=int(realsize)
    print('将在当前目录下生成名为“%s”\n大为“%.4fMiB”的随机文件，确定？(y/n)'%(name,realsize/1024/1024),end='')
    choi=input()
    if choi=='y':
        break
    pass
i=0
while realsize>0:
    if realsize>67108864: #当剩余字节大于64MiB时先“组合”再“输出”
        a=[]
        c=1
        while c<=67108864:
            b=random.randint(0,255)
            a.append(b)
            realsize-=1
            c+=1
            pass
        print('已生成64MiB')
        file=open('./'+name,'ab')
        file.write(bytes(a))
        file.close()
    else:
        a=[]
        while realsize>0:
            b=random.randint(0,255)
            a.append(b)
            realsize-=1
            pass
        file=open('./'+name,'ab')
        file.write(bytes(a))
        file.close()
        pass
    pass
input('完成')