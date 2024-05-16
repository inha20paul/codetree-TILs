n1,n2=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans=False

for i in range(n1):
    if A[i]==B[0]:
        if A[i:i+n2]==B:
            ans=True

if ans:
    print("Yes")
else:
    print("No")