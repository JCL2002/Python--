c=int(input('请输入想要累加的个数：'))
i=0
inp=[]
while i<c:
    count=c-i
    rec=int(input('再请输入%d个数：'%count))
    inp.append(rec)
    i+=1
    pass
def summer(inp):
    s=0
    for i in inp:
        s+=i
        pass
    print( "这些数字的和为：%s"%s)
summer(inp)
input('按回车键退出')