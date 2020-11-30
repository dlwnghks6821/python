import re 
p = re.compile('[a-z]+')
'''
m = p.match("3python")
print(m)
m = p.search("3python")
print(m)
m = p.findall("life is too short")
print(m)

m = p.finditer("life is too short")
print(m)
for i in m:
  print(i)
'''
#match 객체의 메서드
m = p.match("python")
print(m.group())#매치된 문자열을 돌려준다.
print(m.start())#매치된 문자열의 시작위치를 돌려준다.
print(m.end())#매치된 문자열의 끝위치를 돌려준다.
print(m.span())#매치된 문자열의 시작, 끝위치를 튜플로 돌려준다.
