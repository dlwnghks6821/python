
class Menu:
    
    q=0
    
    dic = {}
    str=None
    def buildMenu(self):
       
        import os.path
        file ='d:/menu.txt'
        dic={}
        if(os.path.isfile(file)==True):
            f=open('d:/menu.txt','r')
            line = f.readline()
            while line:
                s=line.split(',')
                self.dic[s[0]]=int(s[1])  
                print(line,end="")
                line=f.readline()
            f.close()
        else:
            print("debug1")
            print("debug2")
            f=open('d:/menu.txt','w')
            p1=input("�޴��� �Է����ּ���.")
            while(p1!=""):
                self.dic[p1]=0
                p2=input("������ �Է����ּ���.")
                self.dic[p1]=int(p2)
                str=p1
                str=str+","+p2
                p1=input("�޴��� �Է����ּ���.")
                f.write(str+'\n')
                print(self.dic)
            f.close()
            
    def showMenu(self):
        for x,y in self.dic.items():
            print(x+":"+str(y))
    
    def Menu2(self):
        global va1
        va1=0
        menu = """
        ... 
        ... ī��� 2000��
        ... īǪġ�� 3000��
        ... �Ƹ޸�ī�� 2000��
        ... ��׷��� 2400��
        ... Enter number: """
        prompt = """
        ... 1. �ֹ�
        ... 2. �ֹ�����
        ... 3. �Ѹ��⺸��
        ... 4. �޴�����
        ... 5. �߰�
        ... 6. ����
        ... 7.������
        ... Enter number: """
        global total
        global str
        v8=[]
        total=0
        dic2={}
        dic3={}
       
        sum=0
        number=0
        p1=[2400,2000,3000,2400]
        m1=['ī���','īǪġ��','�Ƹ޸�ī��','��׷���']
        c1=[]
        m2=[]
        total1=[]
        while(number!=7):
            print(prompt)
            print(self.dic)
            number=int(input())
            if(number==1):
                f=open('d:/menu.txt','r')
                line =f.readline()
                while line:
                    print(line,end="")
                    line=f.readline()
                f.close()
                number2=int(input("select Menu ��Ҵ�5��Ű"))
                while(number2!=5):
                    a=number2
                    m2.append(a)
                    dic2[a]=0
                    number3=int(input("enter count"))
                    b=number3
                    dic2[a]=[b]
                    c1.append(b)
                    number2=int(input("select Menu ��Ҵ�5��"))
                    total = p1[a]*b
                    sum=sum+total
                    v8.append((m1[a],b,total))
                for i in v8:
                    print(i[0]+","+str(i[1])+str(i[2]))
                print("�Ѿ�",sum,"��")
                total1.append(total)
            elif(number==2):
                for i in v8:
                        print(i)
            elif(number==3):
                print("������ �Ѹ���",sum,"��")
            elif(number==4):
                f=open('d:/menu.txt','w')
                va3=(input("������ �޴��� �Է����ּ���.��Ҵ� ����"))
                while(va3!=""):
                    del self.dic[va3]
                    print(self.dic)
                    va2=(input("���ο� �޴��� �Է����ּ���."))
                    self.dic[va2]=0
                    va4=(input("���ο� ������ �Է����ּ���."))
                    self.dic[va2]=va4
                    vf=va2
                    vf=str(va2)+","+va4
                    va3=(input("������ �޴��� �Է����ּ���.��Ҵ� ����"))
                    f.write(vf+'\n')
                for x,y in self.dic.items():
                            print(x+":"+str(y))
                f.close()
            elif(number==5):
                f=open('d:/menu.txt','w')
                v13=(input("�߰��� �޴��� �Է��ϼ���."))
                while(v13!=""):
                    self.dic[v13]=0
                    v14=(input("�߰��� ������ �Է��ϼ���."))
                    self.dic[v13]=v14
                    q1=v13
                    q1=str(v13)+","+v14
                    v13=(input("�߰��� �޴��� �Է��ϼ���.��Ҵ� ����"))
                    f.write(q1+'\n')
                for x,y in self.dic.items():
                            print(x+":"+str(y))
            elif(number==6):
                d8=input(("������ �޴��� �Է����ּ���.��Ҵ� ����"))
                while(d8!=""):
                    del self.dic[d8]
                    d8=input(("������ �޴��� �Է����ּ���.��Ҵ� ����"))
                for x,y in self.dic.items():
                            print(x+":"+str(y))
                    
                    

                

                


        
menu = Menu()
menu.buildMenu()
menu.Menu2()



