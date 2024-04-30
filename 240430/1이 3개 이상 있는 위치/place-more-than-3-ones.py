# 격자받기
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
ans=0
# 동서남북
dxs=[1,-1,0,0]
dys=[0,0,-1,1]
#범위 체크
def in_range(x,y):
    return 0<=x<=n-1 and 0<=y<=n-1

for x in range(n):
    for y in range(n):
        cnt=0
        for dx,dy in zip(dxs,dys):
            nx=x+dx
            ny=y+dy
            if not in_range(nx,ny):
                continue
            cnt+=arr[nx][ny]
        if cnt>=3:
            ans+=1

print(ans)