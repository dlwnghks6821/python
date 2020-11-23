#이스케이프 코드 #
a="He 've heard \" hello world\""
print(a)
#문자열에 곱하기가 가능하다.
#ex) a ="hello" a*2 ==> hello hello 
a = "hello"
a*2
a="hello world"
b=a*3
print("-"*50)
#문자열길이 
print(len(a))
#문자열 인덱싱
a[0]


#슬라이싱 기법
print(a[6:11])

a="spring,summer,automn,winter"
print(a[0:6])
print(a[7:13])
print(a[14:20])
print(a[21:27])
a="나랏말씀이 중국과 달라"
print(a[5:12])
a="life is too short"
#처음부터 끝까지 출력
a[:17]
a="asd"
#여러줄을 변수에 넣을때
a="pithon"
a="fwqfwqfwq"
a+="afafwafawfwa"
print(a)
a=a[0]+'y'+a[2:]
#문자열 사이에 추가
print(a)
a="hello world"
a[:5]+"-"+a[6:]
print(a)
#문자열 포매팅
#숫자 넣기
b="I eat %d apples."%3
print(b)
#문자넣기
b="I eat %s apples." %"five"
print(b)
#여러개 하기
b="I eat %d apples and I have %d peaches" %(3,5)
print(b)
#format 사용
b="I eat {0} apples".format(3)
print(b)
#위치 알려주기
a = "hello world"
a.find("d")
#(join==>문자 사이에 문자를 넣음)
",".join('abcd')
a="hello world"
a.upper()
a.lower()
a=10
#문자열바꾸기(replace)
a="hello world"
a.replace("world","word")
b="I have a apple, a pineapple,an ear plug"
b.replace("a","an")
#list슬라이싱
a=[1,2,3,4]
a[0:2]#1,2가 찍히게된다#
a="12345"
a=[0:2]
#sort 정렬
a=[1,4,3,2]
a.sort()
#위치 반환 (index)
a=[1,2,3]
a.index(3)
#리스트에 요소 삽입(insert)

a=[1,2,3]
#index 0 자리에 4를 넣는다.
a.insert(0,4)
a.insert(3,200)
a
#리스트 요소 제거(remove)
a = [1,2,3]
#del 과 remove차이
#del list[index]
#list.remove(value)

#리스트 요소 끄집어내기(pop)
#pop은 리스트의 맨마지막 요소를 돌려주고 그나머지를 지운다.
a=[1,2,3]
a.pop()
a.append(4)#===> 추가해줌 
a
#n=a.pop(index)==>값을 꺼내고 그위치를 지운다.
#튜플과 리스트의 차이점
#튜플은 변경 불가 리스트는 가능
#튜플 리스트 둘다 index가능
#튜플 리스트 둘다 +*가능
