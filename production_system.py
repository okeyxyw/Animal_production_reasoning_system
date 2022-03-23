import numpy as np

class productionSystem:
    def __init__(self):
        f=open("目标数据库TB.txt","r",encoding='utf8')
        self.productions=[]
        self.charicters=[]
        self.myclass=(f.readline().strip("最终类别为：").strip()).split("，")
        f.close()
        f=open("规则数据库RB.txt","r")
        for line in f.readlines():
            if(line!='\n'):
                line=line.replace("->"," ")
                line=line.replace(","," ")
                line=line.split()
                self.productions.append(line)
                for ch in line:
                    if (ch not in self.myclass) and (ch not in self.charicters):
                        self.charicters.append(ch)
        f.close()
    def showProduction(self):
        print()
    def match(self,x):
        for ch in self.productions[x][:-1]:
            if(ch in self.work):
                continue
            else:
                return False
        return True
    def classify(self,work):
        used=np.zeros(len(self.productions))
        counter=len(self.work)
        #self.s=[]
        f=open('综合数据库DB.txt','a')
        f.write('\n推理规则:\n')
        while(True):
            for i in range(len(self.productions)):
                if(used[i]==0 and self.match(i)):
                    used[i]=1
                    # print ('IF ')
                    #print((self.productions[i][:-1]),'-->',self.productions[i][-1])
                    STR=''
                    for J in self.productions[i][:-1]:
                        STR+=J
                        if J!=self.productions[i][-2]:
                            STR+=' AND '
                    f.write('   IF '+STR+' THEN '+self.productions[i][-1]+'\n')
                    print(' IF ',STR,' THEN ',self.productions[i][-1])
                    self.work.append(self.productions[i][-1])
                    if(self.work[-1] in self.myclass):
                        return True
            tmp=len(self.work)
            if(tmp==counter):
                return False
            else:
                counter=tmp
        #f.close()
    def dowork(self):
        print("目标数据库TB：所有类别有:")
        for t in self.myclass:
            print('{:<10}'.format(t),end="")
        print()
        print("所有属性有：")
        counter=0
        for t in self.charicters:
            counter+=1
            if(counter%5==0):
                print('{:<10}'.format(t))
            else:
                print('{:<10}'.format(t),end="")
        self.work=input("\n综合数据库DB-请输入属性(属性之间用空格隔开):\n")
        self.work=self.work.split()
        st='属性'+str(self.work)
        f = open('综合数据库DB.txt', 'a')
        f.write('\n\n\n')
        f.write(st)
        f.close()
        if(self.classify(self.work)):
            f = open('综合数据库DB.txt', 'a')
            print("该物种为："+self.work[-1])
            f.write("该物种为："+self.work[-1]+'\n')
            f.close()
        else:
            f = open('综合数据库DB.txt', 'a')
            print("抱歉，未能识别出该物种\n")
            f.write("抱歉，未能识别出该物种\n")
            f.close()
def main():
    p=productionSystem()
    p.dowork()
if __name__=="__main__":
    print('动物式产生推理系统open!!!!')
    c=0
    # f=open('综合数据库DB.txt','w')
    # while(True):
        # print("-----------------------------------------")
        # s=str(c)+'\n\n'
        # print(s)
        # f.write(s)
    main()
    # c+=1
    print('-----------------------------------------')
    print('写入"综合数据库DB.txt"成功！！！！！')
    print('-----------------------------------------')
    print('end!!')
    # f.close()
