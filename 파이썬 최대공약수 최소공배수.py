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
        n1 = num1/i
        n2 = num2/i

print(d)
print(d*n1*n2)