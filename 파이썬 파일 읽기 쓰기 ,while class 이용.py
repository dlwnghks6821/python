#class ���� ���޼ҵ�� self �� ����Ѵ�.
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
#��������� ����Ҷ��� ��ü �ڽ��� ����Ű�� self�� �Ἥ ����ؾ��Ѵ�.
'''
class Fourcal:
    #������
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
#����� �޾����Ƿ� �θ�Ŭ������ ������� �ڽ��� ����Ҽ��ִ�.
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
#���
class Car:
    pass
#����Ҷ��� ��ȣ�ȿ� ����ϴ�(�θ�Ŭ����)�� �ִ´�.
class Truck(Car):
'''
'''
#Ŭ��������
class Family:
    fname="1"
    def __init__(self):
        self.fname=3

park= Family()
kim=Family()
print(park.fname,kim.fname)
Family.fname = "2"
print(park.fname,kim.fname)
#�޼ҵ忡�� self �� �̿��ؼ� ���� �ٲٸ� ��������� �۵�
#�޼ҵ忡�� ���� �ٲ��� ������  static Ŭ���� �����ν� �۵�
'''
import os.path
file ='d:/caffe-1.txt'
class Menu:
    dic = {}
    str=None
    def buildMenu(self):
        #menu.textȭ���� �����ϴ� ��Ȯ��
        #�������������� ���� �о���δ�(input())
        #menu.txt���� �о�鿩�� dictionary�� �����
        #{�޴�:����,�޴�:����,�޴�:����}
        f=open('d:/caffe-2.txt','w')
        if (os.path.isfile(file)!=f):
            p1=input("�޴����Է����ּ���.")
            while(p1!=""):
                self.dic[p1]=0
                p2=input("�������Է����ּ���.")
                self.dic[p1]=p2
                str=p1
                str=str+","+p2
                p1=input("�޴����Է����ּ���.")
                f.write(str+'\n')
            f.close()
        f=open('d:/caffe-1.txt','r')
        line =f.readline()
        while line: 
            print(line,end="")
            line=f.readline()
        f.close()
        print("����")
        
    
    def showMenu(self):
        #dictionary���� ȭ�鿡 ǥ��
        print(self.dic)

menu = Menu()
menu.buildMenu()
menu.showMenu()



    




