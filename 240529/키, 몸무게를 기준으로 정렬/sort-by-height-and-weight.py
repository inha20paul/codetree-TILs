n=int(input())
p=[]
for i in range(n):
    name,h,w=input().split()
    p.append((name,int(h),int(w)))

p.sort(key=lambda x:(x[1],-x[2]))
for name,h,w in p:
    print(name,h,w)