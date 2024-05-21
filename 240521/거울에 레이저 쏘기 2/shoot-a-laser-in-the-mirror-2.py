# 입력부
N=int(input())
arr=[input() for _ in range(N)]
k=int(input())

# 초기위치 r,c
d=(k-1)//N # 초기 입력 방향 (상우하좌)
if d==0:
    r=0
    c=(k-1)%N
elif d==2:
    r=N-1
    c=(N-1)-(k-1)%N
elif d==3:
    r=(N-1)-(k-1)%N
    c=0
else:
    r=(k-1)%N
    c=N-1

# 격자범위
def inRange(r,c):
    return 0<=r<=N-1 and 0<=c<=N-1

# 상,우,하,좌
dc=[0,1,0,-1]
dr=[-1,0,1,0]

# \모양거울 방향전환
m={
    0:1,
    1:0,
    2:3,
    3:2
}

# 방향 반전
back={
    0:2,
    1:3,
    2:0,
    3:1
}

def nextP(r,c,dirr):
    # 종료조건
    if not inRange(r,c):
        return 0
    if arr[r][c]=='/':  #'/'거울
        # 방향 전환
        dirr=(3-dirr)%4
    else: #'\' 거울
        # 방향전환
        dirr=m[dirr]
    nr,nc=r+dr[dirr],c+dc[dirr] # 다음격자
    dirr=back[dirr] # 방향 반전
    return nextP(nr,nc,dirr)+1

print(nextP(r,c,d))