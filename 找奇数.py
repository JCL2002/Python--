c=int(input('请输入想要寻找的个数：'))
i=0
inp=[]
while i<c:
    count=c-i
    rec=int(input('再请输入%d个数：'%count))
    inp.append(rec)
    i+=1
    pass
def jishu(inp):
    opt=[]
    for i in inp:
        tst=i%2
        if tst!=0:
            opt.append(i)
            pass
        pass
    return opt
    pass
print(jishu(inp))
input('按回车键退出')