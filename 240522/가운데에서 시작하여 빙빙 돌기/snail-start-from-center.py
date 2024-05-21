n=int(input())
arr=[[0]*n for _ in range(n)]

num=int((n+1)/2)
#시작= 격자 중앙
r,c=num-1,num-1

# 오른쪽,위,왼쪽,아래
dirr=0
dr=[0,-1,0,1]
dc=[1,0,-1,0]

cnt=1

for i in range(1,n):
    for j in range(2):
        for k in range(i):
            arr[r][c]=cnt
            r=r+dr[dirr]
            c=c+dc[dirr]
            cnt+=1
        dirr=(dirr+1)%4

for i in range(n):
    arr[r][c]=cnt
    r=r+dr[dirr]
    c=c+dc[dirr]
    cnt+=1


for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()