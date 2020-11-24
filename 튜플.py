str = 'I have a dream today.'
a = str[9:14]
print(a)

str='hi'
'%10s'%str
'%-10s'%str

a = '{0} have {1}apples'.format("I",8)
print(a)
a ='I have a {0}ream'.format("g")
print(a)

#튜플을 이용한 데이터 교환
x=10
y=100
x,y = y,x
print(x),print(y)