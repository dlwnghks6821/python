#�̽������� �ڵ� #
a="He 've heard \" hello world\""
print(a)
#���ڿ��� ���ϱⰡ �����ϴ�.
#ex) a ="hello" a*2 ==> hello hello 
a = "hello"
a*2
a="hello world"
b=a*3
print("-"*50)
#���ڿ����� 
print(len(a))
#���ڿ� �ε���
a[0]


#�����̽� ���
print(a[6:11])

a="spring,summer,automn,winter"
print(a[0:6])
print(a[7:13])
print(a[14:20])
print(a[21:27])
a="���������� �߱��� �޶�"
print(a[5:12])
a="life is too short"
#ó������ ������ ���
a[:17]
a="asd"
#�������� ������ ������
a="pithon"
a="fwqfwqfwq"
a+="afafwafawfwa"
print(a)
a=a[0]+'y'+a[2:]
#���ڿ� ���̿� �߰�
print(a)
a="hello world"
a[:5]+"-"+a[6:]
print(a)
#���ڿ� ������
#���� �ֱ�
b="I eat %d apples."%3
print(b)
#���ڳֱ�
b="I eat %s apples." %"five"
print(b)
#������ �ϱ�
b="I eat %d apples and I have %d peaches" %(3,5)
print(b)
#format ���
b="I eat {0} apples".format(3)
print(b)
#��ġ �˷��ֱ�
a = "hello world"
a.find("d")
#(join==>���� ���̿� ���ڸ� ����)
",".join('abcd')
a="hello world"
a.upper()
a.lower()
a=10
#���ڿ��ٲٱ�(replace)
a="hello world"
a.replace("world","word")
b="I have a apple, a pineapple,an ear plug"
b.replace("a","an")
#list�����̽�
a=[1,2,3,4]
a[0:2]#1,2�� �����Եȴ�#
a="12345"
a=[0:2]
#sort ����
a=[1,4,3,2]
a.sort()
#��ġ ��ȯ (index)
a=[1,2,3]
a.index(3)
#����Ʈ�� ��� ����(insert)

a=[1,2,3]
#index 0 �ڸ��� 4�� �ִ´�.
a.insert(0,4)
a.insert(3,200)
a
#����Ʈ ��� ����(remove)
a = [1,2,3]
#del �� remove����
#del list[index]
#list.remove(value)

#����Ʈ ��� �������(pop)
#pop�� ����Ʈ�� �Ǹ����� ��Ҹ� �����ְ� �׳������� �����.
a=[1,2,3]
a.pop()
a.append(4)#===> �߰����� 
a
#n=a.pop(index)==>���� ������ ����ġ�� �����.
#Ʃ�ð� ����Ʈ�� ������
#Ʃ���� ���� �Ұ� ����Ʈ�� ����
#Ʃ�� ����Ʈ �Ѵ� index����
#Ʃ�� ����Ʈ �Ѵ� +*����
