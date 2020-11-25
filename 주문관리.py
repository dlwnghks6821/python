menu = """
... 0.밀크쉐이크 2400원
... 1.카페라떼 2000원
... 2.카푸치노 3000원
... 3.아메리카노 2000원
... 4.얼그레이 2400원
... Enter number: """
prompt = """
... 1. 주문
... 2. 주문내역
... 3. 총매출보기
... 4. 나가기
... 
... Enter number: """

global total
global total1
global sum
def Menu():
    global total
    total=0
    sum = 0
    number = 0
    p1 = [2400, 2000, 3000, 2400]
    m1 = []
    c1 = []
    total1 = []
    
    while (number != 4):
        print(prompt)
        number = int(input())
        if (number == 1):
            print(menu)
            number2 = int(input("select menu (back:5)"))
            while (number2 != 5):
                a = number2
                m1.append(number2)
                number3 = int(input("enter count"))
                c1.append(number3)
                number2 = int(input("select menu (back:5)"))
                total=p1[a] * number3
                sum=sum+total
            total1.append(total)
        elif (number == 2):
            print(m1, "번메뉴", c1, "잔",total1)
        elif (number ==3):
          print("오늘의 총매출",sum,"원")
Menu()
            
