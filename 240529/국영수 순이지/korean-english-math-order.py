n=int(input())
arr=[]
for i in range(n):
    n,k,e,m=input().split()
    k,e,m=int(k),int(e),int(m)
    tup=(n,k,e,m)
    arr.append(tup)
arr.sort(key=lambda x: (x[1],x[2],x[3]))
arr=arr[::-1]

for name,korean,eng,math in arr:
    print(name,korean,eng,math)