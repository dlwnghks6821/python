#class 안의 모든메소드는 self 를 써야한다.
'''
class Car:
    color="red"
    price=2000
    def showme(self,color,price=7000):
        self.color=color
        self.price=price
        print(color,self.color)
        print(price,self.price)
truck = Car()
truck.showme('blue')
'''
#멤버변수를 사용할때는 객체 자신을 가리키는 self를 써서 사용해야한다.
'''
class Fourcal:
    #생성자
    def __init__(self):
        self.first=0
        self.second=0
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def setdata(self,a,b):
        self.first=a
        self.second=b
    def plus(self):
        return self.first+self.second
    def minus(self):
        return self.first-self.second
    def multiple(self):
        return self.first*self.second
    def divide(self):
        return self.first/self.second

class moreFourCal(Fourcal):
    def power(self):
        return self.first**self.second

fc=Fourcal(12,3)
#fc.setdata(12,3)
x=fc.plus()
print(x)
x=fc.minus()
print(x)
x=fc.multiple()
print(x)
x=fc.divide()
print(x)
mfc = moreFourCal(12,3)
#상속을 받았으므로 부모클래스의 모든기능을 자식이 사용할수있다.
print(mfc.power())
print(mfc.plus())
print(mfc.minus())
print(mfc.multiple())
print(mfc.divide())


'''
'''
class Car:
    def __init__():
        pass
'''
'''
#상속
class Car:
    pass
#상속할때는 괄호안에 상속하는(부모클래스)를 넣는다.
class Truck(Car):
'''
'''
#클래스변수
class Family:
    fname="1"
    def __init__(self):
        self.fname=3

park= Family()
kim=Family()
print(park.fname,kim.fname)
Family.fname = "2"
print(park.fname,kim.fname)
#메소드에서 self 를 이용해서 값을 바꾸면 멤버변수로 작동
#메소드에서 값을 바꾸지 않으면  static 클래스 변수로써 작동
'''
import os.path
file ='d:/caffe-1.txt'
class Menu:
    dic = {}
    str=None
    def buildMenu(self):
        #menu.text화일이 존재하는 지확인
        #존재하지않으면 값을 읽어들인다(input())
        #menu.txt에서 읽어들여서 dictionary를 만든다
        #{메뉴:가격,메뉴:가격,메뉴:가격}
        f=open('d:/caffe-2.txt','w')
        if (os.path.isfile(file)!=f):
            p1=input("메뉴를입력해주세요.")
            while(p1!=""):
                self.dic[p1]=0
                p2=input("가격을입력해주세요.")
                self.dic[p1]=p2
                str=p1
                str=str+","+p2
                p1=input("메뉴를입력해주세요.")
                f.write(str+'\n')
            f.close()
        f=open('d:/caffe-1.txt','r')
        line =f.readline()
        while line: 
            print(line,end="")
            line=f.readline()
        f.close()
        print("종료")
        
    
    def showMenu(self):
        #dictionary내용 화면에 표시
        print(self.dic)

menu = Menu()
menu.buildMenu()
menu.showMenu()



    




