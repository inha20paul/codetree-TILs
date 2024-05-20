n=int(input())
memo=[0]*(n+1)

def f(n):
    if n==1 or n==-1:
        return 0
    if n==0:
        return 1
    if memo[n]==0:
        memo[n]=f(n-2)+f(n-3)
    return memo[n]

print(f(n)%10007)