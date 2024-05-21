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
limit=min(len(arrA),len(arrB))-1

for i in range(1,check):
    if len(arrA)<=len(arrB):
        if i<=limit:
            if arrA[i]==arrB[i] and arrA[i-1]!=arrB[i-1]:
                cnt+=1
                
        else:
            if arrA[limit]==arrB[i]:
                cnt+=1
                
    else:
        if i<=limit:
            if arrA[i]==arrB[i] and arrA[i-1]!=arrB[i-1]:
                cnt+=1
            
        else:
            if arrA[i]==arrB[limit]:
                cnt+=1
                

print(cnt)