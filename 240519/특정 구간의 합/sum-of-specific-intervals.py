n,m=map(int,input().split())
A=list(map(int,input().split()))

def f(m):
    global A
    for i in range(m):
        a1,a2=map(int,input().split())
        print(sum(A[a1-1:a2]))

f(m)