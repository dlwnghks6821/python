import os
from menu import Menu


#����� ����
'''
1. ����κ� �ߺ����Ǹ� ����
2.���α׷� ũ�� ����
3.����κ��� �����.

'''
menu=Menu()
menu.buildMenu()

job=input('�۾��� �����ϼ��� (�ֹ�:o,����:s,�޴�����:m,����:x)')
while(job!='x'):
    if job=='o':
        menu.showMenu()
        n=input('(����:Enter) �޴���ȣ:')  # ����� ���α׷���(Defensive Programming)
        while n:
            if n.isnumeric():
                cnt=input('����: ')
                while not cnt.isnumeric():
                    cnt=input('����: ')

                lMenu=[]; lCount=[]; lPrice=[]
                n=int(n)
                i=0
                for name,price in menu.dMenu.items():
                    n+=1
                    if n==i:
                        lMenu.append(name)
                        lCount.append(int(cnt))
                        lPrice.append(price*int(cnt))
                        break
                
            n=input('(����:Enter) �޴���ȣ:')
        # �ֹ��������̱�
        i=0
        print('-'*10); print('�ֹ�����'); print('-'*30)
        for name in lMenu:
            print(name+","+str(lCount[i])+","+str(lPrice[i]))
            menu.sMenu.append(name)
            menu.sCount.append(lCount[i])
            menu.sPrice.append(lPrice[i])
            i+=1


    elif job=='s':
        print('-'*10); print('���⳻��'); print('-'*30)
        i=0
        for name in menu.sMenu:
            print(name+","+str(menu.sCount[i])+","+str(menu.sPrice[i]))
            i+=1
        if i==0:  # user-friendly (����� ģȭ�� �޼���)
            print('���� ���⳻���� �����ϴ�')

    elif job=='m':
        menu.showMenu()
        n=input('(�޴��߰�:a, �޴�����:u, �޴�����:d, ����:Enter) �۾�����: ')
        while n:
            if n=='a':
                name=input('(����:Enter) �޴��̸�: ')
                while name:
                    price=input('����')
                    while not price.isnumeric():
                        price=input('����')
                    menu.dMenu[name]=int(price)
                    name=input('(����:Enter) �޴��̸�: ')
                f=open(menu.fname,'w')
                for name,price in menu.dMenu.items():
                    f.write(name+','+str(price))
                f.close()
                menu.showMenu()
            elif n=='u':
                name_old=input('(����:Enter) �޴��̸�: ')
                while name:
                    name_new=input('(����:Enter) ���޴��̸�: ')
                    if name_new=='':
                        break;
                    price_new=input('���޴�����: ')
                    while not price_new.isnumeric():
                        price_new=input('���޴�����: ')
                    del menu.dMenu[name_old]
                    menu.dMenu[name_new]=int(price)
                    name_old=input('(����:Enter) �޴��̸�: ')
                f=open(menu.fname,'w')
                for name,price in menu.dMenu.items():
                    f.write(name+','+str(price))
                f.close()
                menu.showMenu()

            elif n=='d':
                name_old=input('(����:Enter) �޴��̸�: ')
                while name_old:
                    del menu.dMenu[name_old]
                    name_old=input('(����:Enter) �޴��̸�: ')
                f=open(menu.fname,'w')
                for name,price in menu.dMenu.items():
                    f.write(name+','+str(price))
                f.close()
                menu.showMenu()    
            n=input('(�޴��߰�:a, �޴�����:u, �޴�����:d, ����:Enter) �۾�����: ')    

    job=input('�۾��� �����ϼ��� (�ֹ�:o,����:s,�޴�����:m,����:x)')
print("Have a nice day !!!")    