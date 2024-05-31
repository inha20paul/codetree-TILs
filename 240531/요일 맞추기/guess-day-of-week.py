m1,d1,m2,d2=map(int,input().split())
day=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
date=1

def countDays(m,d):
    for i in range(m):
        d+=month[i]
    return d

diff=countDays(m2,d2)-countDays(m1,d1)
date= (date+diff)%7

print(day[date])