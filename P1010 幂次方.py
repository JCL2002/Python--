def anyone(i,inp):#从下标i排查到列表的末尾，如果存在1就返回True，否则返回False
	le=len(inp)
	while(i<le):
		if(inp[i]==1):
			return True
		i+=1
		pass
	return False
def mcf(nu):
	bin_list=[]#初始化一个空数组，用于把数值转化为二进制存放
	#当数值为0时不需要转化直接输出
	if(nu==0):
		print("0",end='')
		pass
	else:
		#转化十进制整数为二进制数，保存在列表bin_list中
		while(nu!=0):
			bin_list.append(nu%2)
			nu=int(nu/2)
			pass
		bin_list.reverse()#翻转列表，使得顺序为正常二进制顺序
		test=0#用于计数列表下标，下一次递归时，length-test就是对应的次方数
		length=len(bin_list)
		for i in bin_list:
			test+=1#计数下标（比下标大1）
			if(i==1 and length-test>1):#当次方数大于1时才有必要进行下一轮递归，当小于等于1时直接输出2(0)和2
				print("2(",end='')
				mcf(length-test)#下一轮递归
				print(")",end='')
				if (anyone(test,bin_list)):#判断项后面是不是要加“+”，当列表bin_list从当前位数往后直到结束还有“1”的存在，即当前项不是最后项就要加“+”，此处调用函数anyone
					print("+",end='')
					pass
				pass
			elif(i==1):#当次方数小于1时
				if(length-test==1):
					if(bin_list[-1]!=0):#判断是否要输出“+”
						print("2+",end='')
						pass
					else:
						print("2",end='')
						pass
					pass
				elif(length-test==0):#当为最后一个元素时，一定不输出“+”
					print("2(0)",end='')
					pass
				pass
			pass
		pass
	pass
nu=int(input())#输入要计算的数值
mcf(nu)#调用主函数
