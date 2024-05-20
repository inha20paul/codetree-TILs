N,M=map(int,input().split())
arr=[0]
# A의 현재위치
A=0
# B의 현재위치
B=0
dx={
    'L':-1,
    'R':1
}
ans=0
cnt=0

for i in range(N):
    d,t=input().split()
    t=int(t)
    for j in range(t):
        A+=dx[d]
        # t초일때 A의 위치 저장
        arr.append(A)

for i in range(M):
    if ans!=0:
        break
    d,t=input().split()
    t=int(t)
    for j in range(t):
        B+=dx[d]
        cnt+=1
        if arr[cnt]==B:
            ans=cnt
            break

print(ans)