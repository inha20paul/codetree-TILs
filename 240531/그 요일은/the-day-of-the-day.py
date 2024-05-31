m1,d1,m2,d2=map(int,input().split())
days=["Mon",'Tue','Wed','Thu','Fri','Sat','Sun']
months=[0,31,29,31,30,31,30,31,31,30,31,30,31]
A=input() 
date=0 # 오늘 무슨요일인지 (%7필요)
cnt=0 # A count
while True:
    # 종료조건
    if m1==m2 and d1==d2:
        break
    d1+=1
    date=(date+1)%7
    if days[date]==A:
        cnt+=1
    if months[m1]<d1:
        d1=1
        m1+=1

print(cnt)