n=int(input())
arr=[]
for i in range(n):
    n,k,e,m=input().split()
    arr.append(tuple(n,int(k),int(e),int(m)))
arr.sort(key=lambda x: (x[1],x[2],x[3]))
arr=arr[::-1]

for name,korean,eng,math in arr:
    print(name,korean,eng,math)