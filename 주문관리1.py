import os
from menu import Menu


#모듈의 장점
'''
1. 공통부분 중복정의를 피함
2.프로그램 크기 감소
3.공통부분을 숨긴다.

'''
menu=Menu()
menu.buildMenu()

job=input('작업을 선택하세요 (주문:o,실적:s,메뉴수정:m,종료:x)')
while(job!='x'):
    if job=='o':
        menu.showMenu()
        n=input('(종료:Enter) 메뉴번호:')  # 방어적 프로그래밍(Defensive Programming)
        while n:
            if n.isnumeric():
                cnt=input('수량: ')
                while not cnt.isnumeric():
                    cnt=input('수량: ')

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
                
            n=input('(종료:Enter) 메뉴번호:')
        # 주문내역보이기
        i=0
        print('-'*10); print('주문내역'); print('-'*30)
        for name in lMenu:
            print(name+","+str(lCount[i])+","+str(lPrice[i]))
            menu.sMenu.append(name)
            menu.sCount.append(lCount[i])
            menu.sPrice.append(lPrice[i])
            i+=1


    elif job=='s':
        print('-'*10); print('매출내역'); print('-'*30)
        i=0
        for name in menu.sMenu:
            print(name+","+str(menu.sCount[i])+","+str(menu.sPrice[i]))
            i+=1
        if i==0:  # user-friendly (사용자 친화적 메세지)
            print('아직 매출내역이 없습니다')

    elif job=='m':
        menu.showMenu()
        n=input('(메뉴추가:a, 메뉴수정:u, 메뉴삭제:d, 종료:Enter) 작업선택: ')
        while n:
            if n=='a':
                name=input('(종료:Enter) 메뉴이름: ')
                while name:
                    price=input('가격')
                    while not price.isnumeric():
                        price=input('가격')
                    menu.dMenu[name]=int(price)
                    name=input('(종료:Enter) 메뉴이름: ')
                f=open(menu.fname,'w')
                for name,price in menu.dMenu.items():
                    f.write(name+','+str(price))
                f.close()
                menu.showMenu()
            elif n=='u':
                name_old=input('(종료:Enter) 메뉴이름: ')
                while name:
                    name_new=input('(종료:Enter) 새메뉴이름: ')
                    if name_new=='':
                        break;
                    price_new=input('새메뉴가격: ')
                    while not price_new.isnumeric():
                        price_new=input('새메뉴가격: ')
                    del menu.dMenu[name_old]
                    menu.dMenu[name_new]=int(price)
                    name_old=input('(종료:Enter) 메뉴이름: ')
                f=open(menu.fname,'w')
                for name,price in menu.dMenu.items():
                    f.write(name+','+str(price))
                f.close()
                menu.showMenu()

            elif n=='d':
                name_old=input('(종료:Enter) 메뉴이름: ')
                while name_old:
                    del menu.dMenu[name_old]
                    name_old=input('(종료:Enter) 메뉴이름: ')
                f=open(menu.fname,'w')
                for name,price in menu.dMenu.items():
                    f.write(name+','+str(price))
                f.close()
                menu.showMenu()    
            n=input('(메뉴추가:a, 메뉴수정:u, 메뉴삭제:d, 종료:Enter) 작업선택: ')    

    job=input('작업을 선택하세요 (주문:o,실적:s,메뉴수정:m,종료:x)')
print("Have a nice day !!!")    