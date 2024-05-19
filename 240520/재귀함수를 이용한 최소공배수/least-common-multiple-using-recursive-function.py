n=int(input())
arr=list(map(int,input().split()))

def f(a,b):
    for i in range(1,b+1):
        if (a*i)%b==0:
            return a*i

def g(n):
    if n==0:
        return arr[0]
    return f(arr[n-1],g(n-1))

print(g(n))