#A는 N번, B는 M번 이동
N,M=map(int,input().split())

arrA=[0]
currA=0
arrB=[0]
currB=0

for i in range(N):
    v,t=map(int,input().split())
    for j in range(t):
        currA+=v
        arrA.append(currA)

for i in range(M):
    v,t=map(int,input().split())
    for j in range(t):
        currB+=v
        arrB.append(currB)

prev=''
cnt=0
for i in range(1,len(arrA)):
    if arrA[i]==arrB[i]:
        cur='AB'
    elif arrA[i]>arrB[i]:
        cur='A'
    elif arrA[i]<arrB[i]:
        cur='B'
    if cur!=prev:
        cnt+=1
    prev=cur

print(cnt)