n,m=map(int,input().split())
arr=[[0]*m for _ in range(n)]

# 시작 0,0
r,c=0,0

dirr=0

# 아래,오른쪽,위,왼쪽
dr=[1,0,-1,0]
dc=[0,1,0,-1]

def inRange(r,c):
    return 0<=r<=n-1 and 0<=c<=m-1

for i in range(1,n*m+1):
    arr[r][c]=i
    nr=r+dr[dirr]
    nc=c+dc[dirr]
    if inRange(nr,nc) and arr[nr][nc]==0:
        r,c=nr,nc
    else:
        dirr=(dirr+1)%4
        r=r+dr[dirr]
        c=c+dc[dirr]

# 배열 출력
for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()