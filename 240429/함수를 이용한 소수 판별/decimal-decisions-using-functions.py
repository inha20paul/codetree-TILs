def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
arr=[0]
a,b=map(int,input().split())
for j in range(a,b+1):
    if isPrime(j):
        arr.append(j)
print(sum(arr))