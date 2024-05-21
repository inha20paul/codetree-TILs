n,m=map(int,input().split())
arr=[['']*m for _ in range(n)]

def inRange(r,c):
    return 0<=r<=n-1 and 0<=c<=m-1

r,c=0,0

#오른쪽,아래,왼쪽,위
dirr=0
dr=[0,1,0,-1]
dc=[1,0,-1,0]

for i in range(n*m):
    string=chr(ord('A')+i)
    arr[r][c]=string

    nr=r+dr[dirr]
    nc=c+dc[dirr]
    if inRange(nr,nc) and arr[nr][nc]=="":
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