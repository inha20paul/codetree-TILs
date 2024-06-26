n,t=map(int,input().split())
r,c,d=input().split()
r=int(r)
c=int(c)

#상좌우하
dr=[-1,0,0,1]
dc=[0,-1,1,0]

mapping={
    'U':0,
    'L':1,
    'R':2,
    'D':3
}
#초기방향
dirr=mapping[d]

def inRange(r,c):
    return 1<=r<=n and 1<=c<=n

for i in range(t):
    nr,nc=r+dr[dirr],c+dc[dirr]
    if inRange(nr,nc):
        r,c=nr,nc
    else:
        dirr=(3-dirr)%4

print(r,c)