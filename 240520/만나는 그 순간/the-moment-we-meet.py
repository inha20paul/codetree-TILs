N,M=map(int,input().split())
# A 위치 기록
arrA=[0]
# A의 현재위치
A=0

# B 위치 기록
arrB=[0]
# B의 현재위치
B=0

dx={
    'L':-1,
    'R':1
}

ans=-1


for i in range(N):
    d,t=input().split()
    t=int(t)
    for j in range(t):
        A+=dx[d]
        # t초일때 A의 위치 저장
        arrA.append(A)

for i in range(M):
    d,t=input().split()
    t=int(t)
    for j in range(t):
        B+=dx[d]
        # t초일때 A의 위치 저장
        arrB.append(B)

for i in range(1,len(arrA)):
    if arrA[i]==arrB[i]:
        ans=i
        break

print(ans)