n=int(input())

def f(n):
    if n==1:
        return 0
    return f(n//2)+1 if n%2==0 else f(3*n+1)+1

print(f(n))