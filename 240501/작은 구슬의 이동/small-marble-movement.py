# n:격자크기 t:시간(초)
n,t=map(int,input().split())
# r:행 c:열 d:이동방향
r,c,d=input().split()
r=int(r)
c=int(c)

# 위,왼,우,아래
dx=[0,-1,1,0]
dy=[-1,0,0,1]

# 반대방향끼리 합=3
mapping={
    'U':0,
    'L':1,
    'R':2,
    'D':3
}

direction=mapping[d]

def in_range(r,c):
    return 1<=r<=n and 1<=c<=n

for i in range(t):

    if in_range(r+dy[direction],c+dx[direction]):
        c+=dx[direction]
        r+=dy[direction]
    else:
        direction=3-direction

print(r,c)