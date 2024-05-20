n=int(input())
memo=[-1]*(n+1)

# 세로로 채우기(-1), 가로로 채우기(-2)

def f(n):
    # 종료 조건
    if n<=2:
        return n
    if memo[n]!=-1:
        return memo[n]
    else:
        memo[n]=f(n-1)+f(n-2)
    return memo[n]


print(f(n)%10007)