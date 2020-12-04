n=int(input('几的阶乘：'))
res,i=1,1
while i<=n:
    res*=i
    i+=1
    pass
if n==0:
    print(0)
    pass
else:
    print(res)
    pass
input('按回车键退出')