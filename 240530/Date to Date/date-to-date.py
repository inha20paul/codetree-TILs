m1,d1,m2,d2=map(int,input().split())
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
start=sum(days[:m1])+d1
end=sum(days[:m2])+d2

print(end-start+1)