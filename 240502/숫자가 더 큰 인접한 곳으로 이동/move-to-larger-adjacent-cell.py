n,r,c=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]

def inRange(r,c):
    return 0<=r<=n-1 and 0<=c<=n-1


while True:
    print(arr[r-1][c-1],end=" ")
    maxnum=arr[r-1][c-1]
    dcs=[0,0,-1,1]
    drs=[-1,1,0,0]
    next_r=0
    next_c=0
    for dc,dr in zip(dcs,drs):
        nc=c+dc
        nr=r+dr
        if inRange(nr,nc) and arr[nr-1][nc-1]>maxnum:
            maxnum=arr[nr-1][nc-1]
            next_r,next_c=nr,nc
            break
    if next_r==0 and next_c==0:
        break
    r,c=next_r,next_c