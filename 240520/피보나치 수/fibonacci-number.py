# # Tabulation
# N=int(input())

# dp = [1] * N

# for i in range(2,N):
#     dp[i]=dp[i-1]+dp[i-2]

# print(dp[N-1])

# 피보나치 수열 f(n) = f(n-1) + f(n-2) 

# 메모이제이션
N=int(input())
memo=[-1]*(N+1)

def fibbo(N):
    # 메모이제이션
    if memo[N]!=-1:
        return memo[N]
    # 종료 조건
    if N<=2:
        memo[N]=1
    else:
        memo[N]=fibbo(N-1)+fibbo(N-2)
    return memo[N]

print(fibbo(N))