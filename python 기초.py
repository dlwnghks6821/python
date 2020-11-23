food = "python's favorite food is perl"
print(food)
food = '"python is very easy'" he says."
print(food)
#줄바꿈 방법 
#1)
multi  ='''
life is short
you need python
'''
#2)
print(multi)
multi2 = "life is short \n you need python"
print(multi2)

#문자열 더해서 연결하기 
head = "python"
tail = "is fun"
n = head+tail
print(n)
#문자열 을 곱해보자 
# 원하는 문장/문자 *(n) n==>원하는 횟수
a = "hello world"
p = a*10
print(p)

#문자열의 길이 구하기 
#a = "life is too short"

#len(a)
#print(len(a))
#문자열 인덱싱
a = "life is short, you need python"
a[3]
print(a[3]) 
print(a[-6])

#슬라이싱 기법 
a = "Life is too short, you need python"
#ex) Life 라는 단어만 추출하고 싶을경우 
print(a[0:4])
print(a[8:12])
print(a[12:17])

a = 'You need Python'
print(a[:15])
a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year,day,weather)

#문자열 바꾸기
#파이썬에서 문자열 자료형은 그 요솟값을 변경할 수 없는 immutable 자료형이라고 한다
a = "pithon"
a[:1]
a[2:]
print(a[:1]+"y"+a[2:])

a="polytics"

print(a[0:4]+"i"+a[4:])

#문자열 포맷팅
#숫자를 대입할때는 %d를 대입한다.
a = "I eat %d apples." %3
print(a)
#문자열을 대입할때는 %s 를 대입한다.
b = "I eat %s apples." %"five"
print(b)

number = 10
b = "I eat %d apples"% number
print(b)
#format 함수를 이용한 포매팅
#q = "I eat {0} {1}apples".format(3,4)
#print(q)
f = "I eat {0} {1} {2} ".format(3,"apples","today")
print(f)

#list 만들기 
#==>list ==> 배열

odd = [1,2,3,4,5]
print(odd)
a = [1,2,3,4,5]
print(a[0]+a[3])

a=[1,2,3,['a','b','c']]
#-1 ==>요소의 마지막 값 
print(a[3][0])
print(a[3][1])
print(a[3][2])
#삼중 배열 인덱싱하기 
a = [1,2,['a','b',['life','is']]]
print(a[2][2][1])
#리스트 슬라이싱
a = "12345"
a[0:2]
print(a[0:2])
a=[1,2,3,4,5]
b=a[:2]
c=a[2:]
print(b)
print(c)

#리스트더하기
a = [1,2,3]
b = [4,5,6] 
print(a+b)
#리스트에서 값을 수정하기 
c = [1,2,3]
c[1]=100
print(c)
#del 함수를 이용하여 리스트 요소 삭제하기
a = [1,2,3]
#==> del a[n] ==> a배열의 n번째 인덱스 값을 삭제하겠다라는 뜻
del a[1]
print(a)

q = [1,2,3,4,5]
del q[0:2]
print(q)
f = [1,2,3,4,5]
del f[2:]
print(f)

a = [1,2,3]
a.index(3)
print(a.index(3))
print(a.index(2))

#튜플객체는 삭제를 할수없다 수정을 할수없다 .
#t1 = (1,2,'a','b')
#del t1[0]
#튜플객체는 값을 변경할수없다.
#t1=(1,2,'a','b')
#t1[0]='f'

t1 = (1,2,3,'a','b')
t2 = (3,4)
print(t1[0]+t2[0])
print(t1[1]*t2[1])

#딕셔너리 
person = {'name':'pey','phone':'01064863482','birth':'0005293412119'}
print(person)
human = {
  'name':'pey',
  'phone':'123123123',
  'birth':'01203012321'
}
print(human)

#딕셔너리 쌍 추가 
a= {
  1:'a'
}
a[2] = 'b'
print(a)

g = {1:'a',2:'f'}
g[100] = 'true'
print(g)
#딕셔너리 요소삭제
#키값을 기준으로 삭제 ==> 배열은 인덱스를 기준으로 삭제했었다.//
del g[1]
print(g)
#key값을 이용해서 key에 해당하는 value를 얻는다.//
grade = {'lee':100,'juliet':1}
grade['lee']
print(grade['lee'])
#keylist만들기 ==>key값만을 모아놓은 객체를 생성한다.
#==> 고유의 append,insert,pop,remove,sort(배열에 적용되는 특수한 함수)를 수행할수없다.
a ={'name':'lee','phone':'1231231232','birth':'1118'}
print(a.keys())
#valuelist 만들기 ==> value 값만을 모아놓은 객체를 생성한다.//
a.values()
print(a.values())
#key , value값을 얻는방법(쌍으로 얻기)
print(a.items())

#key:value 쌍 모두 지우기 
print(a.clear())

#집합자료형
s1 = set([1,2,3])
print(s1)
#==>집합 자료형 ==> 1)중복을 허용하지 않는다. 2)순서가 없다.
#3)배열(리스트),튜플은 순서가 있기때문에 인덱스로값을 얻을수 있으나 set(집합자료형)은 순서가 없기 때문에 인덱스로 값을 얻을수 없다.
s2 = set("Hello")
print(s2)