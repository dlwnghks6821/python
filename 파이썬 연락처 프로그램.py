prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """
number = 0 
a = []
while(number!=4):
  print(prompt)
  number = int(input())
  if(number==1):
    number2 = input("추가하실 이름을 입력해주세요")
    while(number2!=""):
      a.append(number2)
      number3 = input("추가하실 성별을 입력해주세요.")
      a.append(number3)
      number4 = input("추가하실 모바일 번호를 입력해주세요.")
      a.append(number4)
      number5 = input("추가하실 주소를 입력해주세요.")
      a.append(number5)
      number2 = input("추가하실 이름을 입력해주세요")
     
      
  elif(number==2):
    number3 = input("삭제하실 내용을 입력해주세요.")
    while(number3!=""):
      a.remove(number3)
      number3 = input("삭제하실 내용을 입력해주세요.")
  elif(number==3):
      print("현재 리스트입니다.")
      print(a)

