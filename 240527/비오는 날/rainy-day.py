n=int(input())
rains=[]

class weather:
    def __init__(self,ymd,day,wth):
        self.ymd=ymd
        self.day=day
        self.wth=wth

for i in range(n):
    ymd,day,wth=input().split()
    if wth=="Rain":
        rains.append(weather(ymd,day,wth))

ymd_list=[w.ymd for w in rains]
ymd_list.sort()

for w in rains:
    if w.ymd==ymd_list[0]:
        print(f'{w.ymd} {w.day} {w.wth}')