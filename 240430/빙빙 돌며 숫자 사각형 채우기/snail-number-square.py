#행,열
n,m=map(int,input().split())

ans=[[0]*m for _ in range(n)]

def in_range(x,y):
    return 0<=x<=m-1 and 0<=y<=n-1

#오른쪽,아래,왼쪽,위
dx=[1,0,-1,0]
dy=[0,1,0,-1]
dirnum=0
x,y=0,0

ans[0][0]=1

for i in range(2,(n*m)+1):
    nx=x+dx[dirnum]
    ny=y+dy[dirnum]
    if not in_range(nx,ny) or ans[ny][nx]!=0:
        dirnum=(dirnum+1)%4
        nx=x+dx[dirnum]
        ny=y+dy[dirnum]
    x,y=nx,ny
    ans[ny][nx]=i

for row in ans:
    for elem in row:
        print(elem,end=" ")
    print()