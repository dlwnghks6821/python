
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

