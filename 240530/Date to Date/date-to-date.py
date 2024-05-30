# m1,d1,m2,d2=map(int,input().split())
# days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
# start=sum(days[:m1])+d1
# end=sum(days[:m2])+d2
# print(end-start+1)

m1,d1,m2,d2=map(int,input().split())
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
cnt=1
while True:
    if m1==m2 and d1==d2:
        break
    d1+=1
    cnt+=1
    if d1==days[m1]:
        d1=0
        m1+=1

print(cnt)