
class Menu:
    q=0
    dic = {}
    str=None
    def buildMenu(self):
        import os.path
        file ='d:/menu.txt'
        if(os.path.isfile(file)==True):
            f=open('d:/menu.txt','r')
            line = f.readline()
            while line:
              
                line=f.readline()
                print(line,end="")
            f.close()
        else:
            print("debug1")
            print("debug2")
            f=open('d:/menu.txt','w')
            p1=input("�޴��� �Է����ּ���.")
            while(p1!=""):
                self.dic[p1]=0
                p2=input("������ �Է����ּ���.")
                self.dic[p1]=p2
                str=p1
                str=str+","+p2
                p1=input("�޴��� �Է����ּ���.")
                f.write(str+'\n')
            f.close()
    def showMenu(self):
        for x,y in self.dic.items():
            print(x+":"+str(y))
    
    def Menu2(self):
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
        ... 5. ������
        ... Enter number: """
        global total
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
        q=0
        w=0
        e=0
        k=0
        l=0
        while(number!=5):
            print(prompt)
            number=int(input())
            if(number==1):
                menu.showMenu()
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
                    v8.append((m1[a],b,"��","��",total,"��"))
                for i in v8:
                    print(i)
                print("�Ѿ�",sum,"��")
                total1.append(total)
            elif(number==2):
                for i in v8:
                        print(i)
            elif(number==3):
                print("������ �Ѹ���",sum,"��")
            elif(number==4):
                f=open('d:/menu.txt','w')
                va1=(input("������ �޴��� �Է����ּ���."))
                while(va1!=""):
                    self.dic[va1]=0
                    va2=(input("������ ������ �Է����ּ���."))
                    self.dic[va1]=va2
                    str=va1
                    str=va1+","+va2
                    va1=(input("������ �޴��� �Է����ּ���."))
                    f.write(str+'\n')
                f.close()


        
menu = Menu()
menu.buildMenu()
menu.showMenu()
menu.Menu2()



