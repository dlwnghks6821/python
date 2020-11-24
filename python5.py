"""
a=[1,2,3]
b=a
id(a)
id(b)
a=[1,2,3]
from copy import copy
b = copy(a)
print(b)
#변수를 만드는 여러방법
#(1.tuple 구조)
a,b = ('python','life')
a
b
a,b = 'python','life'
a
b
a,b,c,d = 'x',10,20,'z'
a 
b 
c
d
#여러개의 변수에 같은값을 대입하기
a=b=c=d='python'
a
b
c
d
"""
#if  else 문
money = True
if money:
    print("Money!")
else:
    print("No money!")


n = 20
if n<10:
    print("hello")
else:
    print("bb")

money = 1000
if money<3000:
    print('3000이하')
elif money>=3000:
    print("3000이상")
else:
    print("~")

i=0
#while i<100:
    print(i)
    i=i+1
#in 의 의미
#in 의 의미1) i가 li 값중 하나인가
i=0
l1=[1,3,5,0,4,6]
if i in l1:
    print(i)
#in 의 의미2)i에 li 값들을 하나씩 넣는다

#for i in l1:
    print(i)

#i =0
#l1 =[1,3,5,0,4,6]
#if i in l1:
    print(i)
#else:
    print("None")


#while i in l1:
    print(i)
#in ==> if 문에서는 check(값을 확인)
#in ==> for 문에서는 assign(값을 넣는다)
#in ==> while 문에서는 assign

#while 문
treeHit = 0
while treeHit < 10:
    treeHit = treeHit+1
    print("나무를%d번 찍었다."%treeHit)
    if treeHit == 10:
        print("나무가 넘어간다.")
#while 문의 활용 1부터 100까지의 합 
sum = 0
i=1
while i<=100:
    sum=sum+i
    i=i+1
    print(sum)
