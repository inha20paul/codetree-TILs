N,M,K=map(int,input().split())
arr=[0]*(N+1)
ans=-1
for i in range(M):
    idx=int(input())
    arr[idx]+=1
    if arr[idx]==K:
        ans=idx
        break

print(ans)