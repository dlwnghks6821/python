"""
sum = 0
i=1
while i<=100:
    sum=sum+i
    i=i+1
    print(sum)
"""
#input()==>문자열로 리턴해줌
#문자열을 정수로 타입캐스팅할때 
#n=input("정수값을 입력해주세요.")
#n=int(n)
#문자로 타입캐스팅할때
#print(n)
#n=str(n)
#두정수를 읽고 최대공약수 최소공배수를 출력
"""
num1=input("정수를 입력해주세요")
num2=input("정수를 입력해주세요")
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
#리스트 내포
'''
'''
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
'''
'''
#for 문 튜플사용
a = [(1,2,3),(4,5,6),(7,8,9)]
for (first,last,third) in a:
    print(first+last+third)
'''
'''
for 문을이용한 최대 최소공배수구하기
d = 0
i = 0
num1=input("정수를 입력해주세요")
num2=input("정수를 입력해주세요")
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
#함수
#def get_number(x,y):
#    n=x*y
#매개변수가 있을때
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
#여러개의 입력값을 받는 함수 만들기
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
#함수에 주어진 매개변수 갯수가 짝수면 더하기
#함수에 주어진 매개변수가 홀수면 곱하기하여서 결과값을 반환하라
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
#튜플을 이용해서 여러개의 값 return 하기
def calc(a,b):
    return(a+b,a*b,a-b,a//b)
a=3
b=7
w,x,y,z=calc(a,b)
print(w,x,y,z)


'''
'''
m=input("정수를 입력해주세요")
n=input("정수를 입력해주세요")
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
    print('최대공약수:{0}','최소공배수:{1}'.format(m,n))
'''
#튜플을 이용한 여러개 return 하기
m=0
n=0
d = 0
n1= 0
n2 = 0
def getCommon(m,n):
    num1=input("정수를 입력해주세요")
    num2=input("정수를 입력해주세요")
    m = int(num1)
    n = int(num2)
    i=1
    for k in range(i,m):
        i=i+1
        if(m%i==0 and n%i==0):
            d=i
        n1 = m/d
        n2 = n/d
    print('최대공약수:{0},최소공배수:{1}'.format(d,d*n1*n2))
    return (d,d*n1*n2)   
a,b=getCommon(m,n)
      