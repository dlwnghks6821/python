"""
a=[1,2,3]
b=a
id(a)
id(b)
a=[1,2,3]
from copy import copy
b = copy(a)
print(b)
#������ ����� �������
#(1.tuple ����)
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
#�������� ������ �������� �����ϱ�
a=b=c=d='python'
a
b
c
d
"""
#if  else ��
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
    print('3000����')
elif money>=3000:
    print("3000�̻�")
else:
    print("~")

i=0
#while i<100:
    print(i)
    i=i+1
#in �� �ǹ�
#in �� �ǹ�1) i�� li ���� �ϳ��ΰ�
i=0
l1=[1,3,5,0,4,6]
if i in l1:
    print(i)
#in �� �ǹ�2)i�� li ������ �ϳ��� �ִ´�

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
#in ==> if �������� check(���� Ȯ��)
#in ==> for �������� assign(���� �ִ´�)
#in ==> while �������� assign

#while ��
treeHit = 0
while treeHit < 10:
    treeHit = treeHit+1
    print("������%d�� �����."%treeHit)
    if treeHit == 10:
        print("������ �Ѿ��.")
#while ���� Ȱ�� 1���� 100������ �� 
sum = 0
i=1
while i<=100:
    sum=sum+i
    i=i+1
    print(sum)
