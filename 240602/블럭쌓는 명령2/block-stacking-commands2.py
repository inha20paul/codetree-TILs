N,K=map(int,input().split())
arr=[0]*N

for i in range(K):
    a,b=map(int,input().split())
    for j in range(a-1,b):
        arr[j]+=1

print(max(arr))