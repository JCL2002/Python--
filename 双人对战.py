class Role:
    def __init__(self,name,hp,tili):
        self.name=name
        self.hp=hp
        self.tili=tili
        #传入角色名字和血量和体力
        pass
    def A(self,enemy): #平A
        self.tili-=10
        enemy.hp-=15
        pass
    def R(self,enemy): #大招
        self.tili-=150
        enemy.hp-=60
        pass#战斗机制：平A自己体力扣10，对方血扣15；大招自己体力扣150，对方血扣60
    def treatment(self): #治疗
        self.tili-=50
        self.hp+=60
        pass#加血，用自己50体力恢复60血
    def relax(self): #休息，恢复25体力
        self.tili+=25
        pass
    pass
mht=Role('马化腾',100,50)
my=Role('马云',100,50)
#初始化人物
i=0
print('平A：0；大招：1；回血：2；休息：3')
while i==0:
    t=input("马化腾过招：")
    if t=='0':
        if mht.tili>=10:
            mht.A(my)
            pass
        else:
            print('体力不够！')
            t=-1
        pass
    elif t=='1':
        if mht.tili>=150:
            mht.R(my)
            pass
        else:
            print('体力不够！')
            t=-1
        pass
    elif t=='2':
        if mht.tili>=50:
            mht.treatment()
            pass
        else:
            print('体力不够！')
            t=-1
    elif t=='3':
        mht.relax()
        pass
    else:
        print('输入错误！')
        continue
    if my.hp<=0:
        input('马化腾胜！')
        exit()
    y=input('马云过招：')
    if y=='0':
        if my.tili>=10:
            my.A(mht)
            pass
        else:
            print('体力不够！')
            y=-1
        pass
    elif y=='1':
        if my.tili>=150:
            my.R(mht)
            pass
        else:
            print('体力不够！')
            y=-1
        pass
    elif y=='2':
        if my.tili>=50:
            my.treatment()
            pass
        else:
            print('体力不够！')
            y=-1
    elif y=='3':
        my.relax()
        pass
    else:
        print('输入错误！')
        continue
    if mht.hp<=0:
        input('马云胜！')
        exit()
    print('马化腾血量：%s 马化腾体力：%s 马云血量：%s 马云体力：%s'%(mht.hp,mht.tili,my.hp,my.tili))
    pass