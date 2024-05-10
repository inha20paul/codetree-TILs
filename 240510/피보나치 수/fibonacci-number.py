N=int(input())

dp = [1] * N

for i in range(2,N):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[N-1])

# 피보나치 수열 f(n) = f(n-1) + f(n-2)