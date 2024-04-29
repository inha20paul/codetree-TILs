def isPrime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    return cnt==2
arr=[0]
a,b=map(int,input().split())
for j in range(a,b+1):
    if isPrime(j):
        arr.append(j)
print(sum(arr))