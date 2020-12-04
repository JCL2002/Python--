import os
import math
Mod=''
#路径输入函数，输入文件名并创建打开,返回路径和打开的文件
def Path_input():
	while True:
		Path=input('请输入文件名/绝对路径：')
		if (os.path.isfile(Path)):
			Mod=''
			break
		elif (Path==''):
			Path='./bitmap'
			Mod='creat'
			File=open(Path,'wb')
			File.close()
			print('在当前目录下创建/覆盖名为"bitmap"的文件')
			break
		else:
			Path_above=Path[:-len(Path.split('/')[-1])] #若文件不存在，则提取其上一级
			if (os.path.isdir(Path_above)):
				print('文件不存在，但是上一级目录存在')
				inp=input('是否新建y/n：')
				if (inp=='y'):
					File=open(Path,'wb')
					File.close()
					Mod='creat'
					break
				else:
					inp=input('是否要退出y/n：')
					if (inp=='y'):
						exit(5)
					pass
			else:
				print('目录不存在！')
				pass
			pass
		pass
	return Path,Mod
	pass
#模式选择
def Mod_input(Mod):
	while (Mod==''):
		Mod=input('请输入模式:打开现有(open)/创建全新(creat)：')
		if (Mod!='open' and Mod!='creat'):
			print('emmm')
			Mod=''
			pass
		else:
			break
		pass
	return Mod
	pass
#输入分辨率
def definition_input():
	while True:
		inp=int(input('请输入边长(一定是正整数，输错会崩溃)：'))
		if (inp>1 and inp<=32):
			return inp
		else:
			print('Are you sure?')
			pass
		pass
	pass
#获取文件大小
def File_size(Path):
	File=open(Path,'rb')
	File.seek(0,2)
	size=File.tell()
	File.close()
	return size
#根据文件大小计算分辨率，文件大小不符合规范返回False
def definition_calculate(size):
	definition=math.sqrt(size)
	definition=str(definition)
	definition_l=len(definition)
	if (definition_l>4):
		return False
	else:
		definition=definition.split('.')[0]
		definition=int(definition)
		return definition
	pass
#显示模块
def Show(Path,definition):
	i=1
	File=open(Path,'rb')
	File.seek(0)
	while (i<=definition):
		j=1
		while (j<=definition):
			bit=File.read(1)
			zero=bytes(1)
			if (bit==zero):
				print('  ',end='')
				pass
			elif (bit==bytes((1,))):
				print(' *',end='')
				pass
			else:
				print('不是由该程序生成的文件或文件损坏')
				exit(5)
			j+=1
			pass
		print('')
		i+=1
		pass
	File.close()
	pass
#全文编辑
def creat_all(Path,definition):
	File=open(Path,'wb')
	i=1
	while (i<=definition):
		Cache=bytes()
		inp=input('第%d行，输入%d个0/1：'%(i,definition))
		if (len(inp)==definition):
			success=True
			for j in inp:
				if (j=='0'):
					Cache+=bytes(1)
					pass
				elif (j=='1'):
					Cache+=bytes((1,))
					pass
				else:
					print('输入有误，只能是0或1')
					input('错误比较难以修复，程序终止，按回车退出')
					File.close()
					exit()
					pass
				pass
			if success:
				File.write(Cache)
				i+=1
				pass
			pass
		else:
			print('长度有误，是%d个'%(definition))
			pass
		pass
	File.close()
	pass
#编辑某一段，当段落超出最大行时返回False，行数小于等于0时，退出程序
def creat_paragraph(Path,definition,paragraph):
	File=open(Path,'rb')
	if (paragraph>definition):
		print('哪有那么多行？')
		return False
	elif (paragraph<=0):
		exit(0)
	else:
		#初始化三段字节存储，防止因空而报错
		Original_above=bytes()
		Original_current=bytes()
		Original_end=bytes()
		#初始化完成，分段存储
		Original_above=File.read((definition*(paragraph-1)))
		Original_current=File.read(definition)
		Original_end=File.read()
		#分段存储完成，关闭读取形式的文件，打开写入模式的文件
		File.close()
		File=open(Path,'wb')
		cycle=True
		while cycle:
			inp=input('第%d行，输入%d个0/1：'%(paragraph,definition))
			if (len(inp)==definition):
				Cache=bytes()
				success=True
				for j in inp:
					if (j=='0'):
						Cache+=bytes(1)
						pass
					elif (j=='1'):
						Cache+=bytes((1,))
						pass
					else:
						print('输入有误，只能是0或1，错误难以修复，程序退出')
						File.close()
						exit(5)
						pass
					pass
				if success:
					Original_current=Cache
					cycle=False
					pass
				pass
			pass
		#写入文件
		File.write(Original_above)
		File.write(Original_current)
		File.write(Original_end)
		File.close()
		pass
	pass
filereturn=Path_input()
Path=filereturn[0]
Mod=filereturn[1]
size=File_size(Path) #取得所指向文件的大小
cycle=True
while cycle:
	Mod=Mod_input(Mod)
	if (Mod=='open'):
		definition=definition_calculate(size)
		if (definition==False):
			print('这个文件不是由该程序生成的或文件损坏！')
			input('按回车键退出程序')
			exit(1)
			pass
		else:
			Show(Path,definition)
			while cycle:
				inp=int(input('请输入要编辑的行号(必须是正整数)，零或负数退出程序：'))
				creat_paragraph(Path,definition,inp)
				Show(Path,definition)
				inp=input('还要继续改吗？(y/n)')
				if (inp=='n'):
					cycle=False
					pass
				elif (inp=='y'):
					pass
				else:
					print('默认你不想了…')
					cycle=False
			pass
		pass
	elif (Mod=='creat'):
		definition=definition_input()
		creat_all(Path,definition)
		cycle=False
		pass
	pass
#位图编辑器
#作者：姜春磊
#时间：2020/11/14-2020/11/15
