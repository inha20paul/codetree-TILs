n,m=map(int,input().split())
A=list(map(int,input().split()))

ans=0

def f():
    global m
    global ans
    while m!=1:
        ans+=A[m-1]
        if m%2==1:
            m-=1
        else:
            m=int(m/2)
    ans+=A[0]


f()
print(ans)