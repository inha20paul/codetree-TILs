#A,B 각각 이동 횟수?
N,M=map(int,input().split())
A=0
arrA=[]
B=0
arrB=[]

for i in range(N):
    v,t=map(int,input().split())
    for j in range(t):
        A+=v
        arrA.append(A)

for i in range(M):
    v,t=map(int,input().split())
    for j in range(t):
        B+=v
        arrB.append(B)

state=''
cnt=-1
for i in range(len(arrA)):
    prev=state
    if arrA[i]>arrB[i]:
        state='A'
    elif arrA[i]<arrB[i]:
        state='B'
    if state!=prev:
        cnt+=1
   
if cnt==-1:
    print(0)
else:
    print(cnt)