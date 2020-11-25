  
prompt = """
... 1. 메뉴추가
... 2. 메뉴삭제
... 3. 메뉴조회
... 4. 메뉴수정
... 5. 나가기
... Enter number: """
number = 0 
a = []
p = []
while(number!=5):
  print(prompt)
  number = int(input())
  if(number==1):
    number2 = input("추가하실 메뉴를 입력해주세요")
    while(number2!=""):
      a.append(number2)
      number3 = input("추가하실 가격을 입력해주세요.")
      p.append(number3)
      number2 = input("추가하실 메뉴를 입력해주세요")
     
  elif(number==2):
    number3 = input("삭제하실 내용을 입력해주세요.")
    while(number3!=""):
      a.remove(number3)
      number3 = input("삭제하실 내용을 입력해주세요.")
  elif(number==3):
      print("현재 리스트입니다.")
      print(a)
      print(p)
  elif(number==4):
    number3 =input("수정할 기존 메뉴의 번호를 입력해주세요.")
    number4 =input("새로운 메뉴를 입력해주세요.")
    a[number3]=str(number4)
