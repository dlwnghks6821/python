import re

p = re.compile('[a-z]+')
#m = p.match("python")
#search ==>  match 와 다르게 처음부터 검색하는것이아니라
#문자열 전체를 검색 하므로 ,앞에 3이 와도 매칭이된다.//
#m = p.search("3python")
#m = p.findall("life is too short")
#==> findall ==> 리스트 로 객체를 돌려준다.//

#==> finditer ==> 이터레이터 객체를 돌려주고 , 그값을 확인하기 위해서는 for문등의 반복문을 통해서 이터레이터 객체의 내용을 알아낼수있다.
#m = p.finditer("life is too short")
#for i in m:
#  print(i)
'''

m = p.match("python")
#==>group() ==> 매치된 문자열을 돌려준다.
print(m.group())
#==>star() ==> 매치된 문자열의 시작위치를 돌려준다.
print(m.start())
#==>end()==>매치된 문자열의 끝위치를 돌려준다.
print(m.end())
#==> span()==>매치된 문자열의 시작과 끝에 해당하는 위치를 튜플로 반환해준다
print(m.span())

'''

'''
#컴파일 옵션
#DOTALL,S  
import re
#==> \n은 포함하지않는다. .과 매치되지않기때문 
p = re.compile('a.b')
m = p.match('a\nb')
print(m)
#매치되게하기위해서는..
p = re.compile('a.b',re.DOTALL)
m = p.match('a\nb')
print(m)
'''
#IGNORECASE I 
p = re.compile('[a-z]',re.I)
p.match('python')
p.match('PYTHON')
print(p.match('python'))
print(p.match('PYTHON'))