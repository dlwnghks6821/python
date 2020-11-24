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
        n1 = num1/i
        n2 = num2/i

print(d)
print(d*n1*n2)