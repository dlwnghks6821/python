
class Menu:
    q=0
    dic = {}
    str=None
    def buildMenu(self):
        import os.path
        file ='D:\\menu.txt'
        if(os.path.isfile(file)==True):
            print("debug")
            f=open('D:\\menu.txt','r')
            line = f.readline()
            while line:
              
                line=f.readline()
                print(line,end="")
            f.close()
        else:
            print("debug1")
            print("debug2")
            f=open('d:/menu.txt','w')
            p1=input("메뉴를 입력해주세요.")
            while(p1!=""):
                self.dic[p1]=0
                p2=input("가격을 입력해주세요.")
                self.dic[p1]=p2
                str=p1
                str=str+","+p2
                p1=input("메뉴를 입력해주세요.")
                f.write(str+'\n')
            f.close()
    def showMenu(self):
        for x,y in self.dic.items():
            print(x+":"+y)
            

        
menu = Menu()
menu.buildMenu()
menu.showMenu()

menu = """
... 0.밀크쉐이크 2400원
... 1.카페라떼 2000원
... 2.카푸치노 3000원
... 3.아메리카노 2000원
... 4.얼그레이 2400원
... Enter number: """
prompt = """
... 1. 주문
... 2. 주문내역
... 3. 총매출보기
... 4. 나가기
... 
... Enter number: """
def Menu():
    global total
    v8=[]
    total=0
    dic2 ={}
    dic3 ={}
    sum = 0
    number = 0
    p1 = [2400, 2000, 3000, 2400,3000]
    m1 = ['밀크쉐이크','카페라떼','카푸치노','아메리카노','얼그레이']
    c1 = []
    m2 = []
    total1 = []
    q=0
    w=0
    e=0
    k=0
    l=0
    while (number != 4):
        print(prompt)
        number = int(input())
        if (number == 1):
            print(menu)
            number2 = int(input("select menu 취소는5"))
            while (number2 !=5):
                a = number2
                m2.append(a)
                dic2[a]=0
                #m1.append(number2)
                number3 = int(input("enter count"))
                b=number3
                dic2[a]=[b]
                c1.append(b)
                number2 = int(input("select menu 취소는 5 "))
                total = p1[a]*b
                #total=p1[a] * number3
                sum=sum+total
                v8.append((m1[a],b,"잔","총",total,"원"))
            for i in v8:
                print(i)
            
            total1.append(total)
        elif (number == 2): 
           for i in v8:
                print(i)
                
        elif (number ==3):
           print("오늘의 총매출",sum,"원")




Menu()

