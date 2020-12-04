#输入部分
while True:
    bit=int(input('请输入要生成的字典的长度：'))
    char=set(input('请输入所用可能出现的字符，仅限英文字母、数字：'))
    file_name=input('请输入用于存储密码字典的文件的名称，该文件将被保存到当前目录下：')
    char_range=len(char)
    char=list(char)
    times=char_range**bit #计算字典密码数量
    size=(bit+1)*times/1024/1024
    choice=input('将要生成的字典包括%d种组合，占用空间%.2fMiB，可能占用较长时间和磁盘空间，是否继续?(y/n)'%(times,size))
    if (choice=='y' or choice=='Y'):
        break
    pass
file=open(file_name,'wb')
#'char'中包括了所有的字符，'bit'中包括了密码长度，'times'表示了要生成的个数，'char_range'包含了密码范围长度
#进制对应部分
def creat(num,h,l=1):
    a=[]
    while l>=1:
        res=divmod(num,h**(l-1)) #计算当前进制位下的商和余数
        consult=res[0]
        num=res[1]
        l-=1
        a.append(consult)
        pass
    return a
def translate(num,form):
    b=''
    for i in num:
        b+=str(form[i])
        pass
    return b
i=0
d=1
while i<times:
    output=translate(creat(i,char_range,bit),char)+'\n'
    file.write(output.encode('utf-8'))
    i+=1
    if i%10000==0:
        print('已生成%d0000个密码'%d)
        d+=1
        pass
    pass
file.close()
input('完成')