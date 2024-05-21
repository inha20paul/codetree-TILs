n,m=map(int,input().split())
dx={
    'L':-1,
    'R':1
}
A=0
arrA=[0]
B=0
arrB=[0]

#A
for i in range(n):
    t,d=input().split()
    t=int(t)
    for j in range(t):
        A+=dx[d]
        arrA.append(A)

#B
for i in range(m):
    t,d=input().split()
    t=int(t)
    for j in range(t):
        B+=dx[d]
        arrB.append(B)
    
cnt=0
check=max(len(arrA),len(arrB))

for i in range(1,check):
    num=min(len(arrA)-1,i)
    if arrA[num]==arrB[i] and arrA[num-1]!=arrB[i-1]:
        cnt+=1

print(cnt)