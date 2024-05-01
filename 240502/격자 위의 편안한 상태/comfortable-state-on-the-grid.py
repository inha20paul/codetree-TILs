N,M=map(int,input().split())
# 격자생성
arr=[[0]*N for _ in range(N)]

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def inRange(r,c):
    return 0<=r<=N-1 and 0<=c<=N-1

def checking(r,c):
    cnt=0
    for dc,dr in zip(dx,dy):
        nc=c+dc
        nr=r+dr
        if inRange(nr,nc) and arr[nr][nc]==1:
            cnt+=1
    return cnt==3

for i in range(M):
    r,c=map(int,input().split())
    # 색칠
    arr[r-1][c-1]=1
    # 체크
    if checking(r-1,c-1):
        print(1)
    else:
        print(0)