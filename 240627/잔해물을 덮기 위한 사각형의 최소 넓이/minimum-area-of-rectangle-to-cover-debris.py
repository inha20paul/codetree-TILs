arr=[[0]*2000 for _ in range(2000)]

x1,y1,x2,y2=map(int,input().split())
x1+=1000
y1+=1000
x2+=1000
y2+=1000
for i in range(x1,x2):
    for j in range(y1,y2):
        arr[i][j]=1

x1,y1,x2,y2=map(int,input().split())
x1+=1000
y1+=1000
x2+=1000
y2+=1000
for i in range(x1,x2):
    for j in range(y1,y2):
        arr[i][j]=0

max_s=[]

for i in range(2000):
    cnt=0
    for j in range(2000):
        if arr[i][j]==1:
            cnt+=1
    if cnt!=0:
        max_s.append(cnt)

ans=len(max_s)*max(max_s)
print(ans)