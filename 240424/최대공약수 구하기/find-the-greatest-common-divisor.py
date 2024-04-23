n,m=map(int,input().split())

def maximum(n,m):
    arr1=[]
    arr2=[]
    for i in range(1,n+1):
        if n%i==0:
            arr1.append(i)
    for i in range(1,m+1):
        if m%i==0:
            arr2.append(i)
    for elem in arr1[::-1]:
        if elem in arr2:
            return elem

print(maximum(n,m))