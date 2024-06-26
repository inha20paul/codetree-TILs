n,m=map(int,input().split())
arr=[[0]*m for _ in range(n)]
size=n*m
# 우,하,좌,상
dr=[0,1,0,-1]
dc=[1,0,-1,0]
r,c=0,0
dirr=0

def inRange(r,c):
    return 0<=r<=n-1 and 0<=c<=m-1

for index in range(1,size+1):
    arr[r][c]=index
    nr,nc=r+dr[dirr],c+dc[dirr]
    if inRange(nr,nc) and arr[nr][nc]==0:
        r,c=nr,nc
    else:
        dirr=(dirr+1)%4
        r,c=r+dr[dirr],c+dc[dirr]

for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()