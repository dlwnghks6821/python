import os

class Menu:
    def __init__(self):
        self.fname="d:/menu.txt"   
        self.sMenu=[] 
        self.sCount=[]
        self.sPrice=[]     
    def buildMenu(self):
        if os.path.isfile(self.fname) == False:
            f=open(self.fname,"w")
            name=input("메뉴이름을 입력하세요 (종료:Enter) ")
            while name:
                price=input("가격을 입력하세요 ")
                f.write(name+","+str(price))
                name=input("메뉴이름을 입력하세요 (종료:Enter) ")
            f.close()
        self.dMenu={}
        f=open(self.fname,'r')  # menu,price
        line=f.readline()
        while line:
            s=line.split(',') # s[0]:메뉴명 s[1]:가격
            self.dMenu[s[0]]=s[1]
            line=f.readline()
        f.close()

    def showMenu(self):
        # dictionary의 내용을 화면에 표시
        print('-'*50)
        n=1
        for name,price in self.dMenu.items():
            print(str(n)+")"+name+":"+str(price), end="")        
            n+=1
        print('\n')
