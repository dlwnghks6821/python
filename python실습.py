"""
sum = 0
i=1
while i<=100:
    sum=sum+i
    i=i+1
    print(sum)
"""
#input()==>���ڿ��� ��������
#���ڿ��� ������ Ÿ��ĳ�����Ҷ� 
#n=input("�������� �Է����ּ���.")
#n=int(n)
#���ڷ� Ÿ��ĳ�����Ҷ�
#print(n)
#n=str(n)
#�������� �а� �ִ����� �ּҰ������ ���
"""
num1=input("������ �Է����ּ���")
num2=input("������ �Է����ּ���")
num1 = int(num1)
num2 = int(num2)

d = 0
i = 0
while i<=num1:
    i=i+1
    if(num1%i==0 and num2%i==0):
        d=i
        n1 = num1/d
        n2 = num2/d

print(d)
print(d*n1*n2)
"""
'''
for i in range(10):
    print(i)
    '''
'''
for i in range(1,11):
    print(i)
sum = 0
for i in range(1,101):
    sum = sum+i
    print(sum)
#����Ʈ ����
'''
'''
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
'''
'''
#for �� Ʃ�û��
a = [(1,2,3),(4,5,6),(7,8,9)]
for (first,last,third) in a:
    print(first+last+third)
'''
'''
for �����̿��� �ִ� �ּҰ�������ϱ�
d = 0
i = 0
num1=input("������ �Է����ּ���")
num2=input("������ �Է����ּ���")
num1 = int(num1)
num2 = int(num2)
for i in range(i,num1):
    i=i+1
    if(num1%i==0 and num2%i==0):
        d=i
        n1 = num1/d
        n2 = num2/d

print(d)
print(d*n1*n2)
'''
#�Լ�
#def get_number(x,y):
#    n=x*y
#�Ű������� ������
'''
def add(x,y):
    return x+y

a=3
b=4
n=add(a,b)
print(n)
'''
'''
def say():
    return "hello"

n = say()
print(n)
'''
'''
def add(x,y):
    return x+y
x=3
y=7
n=add(x=4,y=8)
print(n)
'''
#�������� �Է°��� �޴� �Լ� �����
'''
def add(*ar):
    sum=0
    for i in ar:
        sum=sum+i
    return sum
a=3
b=7
n=add(a,b)
print(n)
c=6
d=10
n=add(a,b,c,d)
print(n)
'''
'''
#�Լ��� �־��� �Ű����� ������ ¦���� ���ϱ�
#�Լ��� �־��� �Ű������� Ȧ���� ���ϱ��Ͽ��� ������� ��ȯ�϶�
def add1(*ar):
    sum=0
    multi = 1
    if(len(ar)%2==0):
        for i in ar:
         sum=sum+i
        return sum
    elif(len(ar)%2!=0):
        for i in ar:
            multi=multi*i
    return multi
a=3
b=7
c=6
n=add1(a,b,c)
print(n)
'''
'''
#Ʃ���� �̿��ؼ� �������� �� return �ϱ�
def calc(a,b):
    return(a+b,a*b,a-b,a//b)
a=3
b=7
w,x,y,z=calc(a,b)
print(w,x,y,z)


'''
'''
m=input("������ �Է����ּ���")
n=input("������ �Է����ּ���")
def getCommon(m,n):
    g=0
    f=0
    d = 0
    i = 1
    a=0
    b=0
    num1 = int(m)
    num2 = int(n)
    for i in range(i,num1):
        i=i+1
        if(num1%i==0 and num2%i==0):
            d=i
            n1 = num1/d
            n2 = num2/d
            g=d
            f=d*n1*n2
    return(g,f)
    a,b=getCommon(m,n)
    print('�ִ�����:{0}','�ּҰ����:{1}'.format(m,n))
'''
#Ʃ���� �̿��� ������ return �ϱ�
'''
m=0
n=0
d = 0
n1= 0
n2 = 0
def getCommon(m,n):
    num1=input("������ �Է����ּ���")
    num2=input("������ �Է����ּ���")
    m = int(num1)
    n = int(num2)
    i=1
    for k in range(i,m):
        i=i+1
        if(m%i==0 and n%i==0):
            d=i
        n1 = m/d
        n2 = n/d
    print('�ִ�����:{0},�ּҰ����:{1}'.format(d,d*n1*n2))
    return (d,d*n1*n2)   
a,b=getCommon(m,n)
'''
#�Լ������� �Ű�����
#�Ű������� �̸� �ʱⰪ�� �����ϱ�..
#1)�Ű������� �տ������� default���� �ټ�����. �ݵ�� �޺κп����� �ټ��ִ�.
'''
def say_myself(name,mobile,gender="female"):
    print(name,mobile,gender)
say_myself("John","44421412","male")
say_myself("John","44421412")
#�Լ������� �Ű������� �⺻������ �ְԵǸ� �Լ��� ȣ���Ҷ� ���ڸ� �Ƚ��־������ �����ʴ´�.
def setStudent(name,gender,cname="rose"):
    print(name,gender,cname)
setStudent("Johanson","female")
'''
'''
a = 1
b = 0
def vartest():
    #global b ===> �Լ��ȿ��ִ� ���������� �������� �� �ٲپ���
    global b
    a = a+1
    b = a+1

vartest(a)
print(a,b)
'''
'''
add = lambda a,b: a+b
'''
#���� �����
'''
f=open('d:/xaexal.txt','w')
for i in range(1,11):
    str='%d��° �����Դϴ�.\n'%i
    f.write(str)
    print(str,end=' ')
f.close()
'''
'''
#�б�
f=open('d:/xaexal.txt','r')
# f.write(str+'\n')
line =f.readline()
while line: 
    print(line,end="")
    line=f.readline()
f.close()
'''
'''
f=open('d:/lee1.txt','w')

str1="lee"
str2="0101312312"
str3="cheonan"
str4="star"
f.write(str1+'\n')
f.write(str2+'\n')
f.write(str3+'\n')
f.write(str4+'\n')
print(str1,end=' ')
print(str2,end=' ')
print(str3,end=' ')
print(str4,end=' ')
f.close()

f=open('d:/lee1.txt','r')
# f.write(str+'\n')
line =f.readline()
while line: 
    print(line,end="")
    line=f.readline()
f.close()
'''
prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number=0
a=[]
b=[]
f=open('d:/caffe02.txt','w')
while(number!=4):
    print(prompt)
    number = int(input())
    if(number==1):
        number2=input("�߰��� �޴�")
        while(number2!=""):
            str=number2
            number3=input("����")
            str=str+","+number3
            f.write(str+'\n')
            number2=input("�߰��� �޴�")
        f.close()


f=open('d:/caffe.txt','r')
# f.write(str+'\n')
line =f.readline()
while line: 
    print(line,end="")
    line=f.readline()
f.close()









