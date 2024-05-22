N,T=map(int,input().split())
string=input()
arr=[list(map(int,input().split())) for _ in range(N)]
start=int((N+1)/2)
r,c=start-1,start-1

#위,오른,아래,왼
dirr=0 # 초기방향 위쪽
dr=[-1,0,1,0]
dc=[0,1,0,-1]

mapping={
    'L':-1,
    'R':1
}

ans=0
ans+=arr[r][c]

def inRange(r,c):
    return 0<=r<=N-1 and 0<=c<=N-1

for q in string:
    if q=='F':
        nr=r+dr[dirr]
        nc=c+dc[dirr]
        if inRange(nr,nc):
            r,c=nr,nc
            ans+=arr[r][c]
    else:
        dirr=(dirr+mapping[q])%4

print(ans)