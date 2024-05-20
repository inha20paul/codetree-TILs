N=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=[arr[i]+arr[2*N-i-1] for i in range(N)]

print(max(ans))