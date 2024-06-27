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

start_x,start_y,end_x,end_y=1000,1000,1000,1000

first=True

for i in range(2000):
    for j in range(2000):
        if arr[i][j]==1:
            if first:
                start_x,end_x=j,j
                start_y,end_y=i,i
                first=False
            start_x=min(start_x,j)
            start_y=min(start_y,i)
            end_x=max(end_x,j)
            end_y=max(end_y,i)


s=(end_x-start_x+1) * (end_y-start_y+1)
if start_x==end_x and start_y==end_y:
    s=0
print(s)