# 격자받기
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
cnt=0
# 동서남북
dxs=[1,-1,0,0]
dys=[0,0,-1,1]
#범위 체크
def in_range(x,y):
    return 0<=x<=n-1 and 0<=y<=n-1

for i in range(n):
    for j in range(n):
        num=0
        for dx,dy in zip(dxs,dys):
            x,y=i,j
            x+=dx
            y+=dy
            if in_range(x,y):
                num+=arr[x][y]
        if num>=3:
            cnt+=1

print(cnt)