n,k,T=input().split()
n,k=int(n),int(k)
arr=[]

for i in range(n):
    string=input()
    if string[:len(T)]==T:
        arr.append(string)

arr.sort()
print(arr[k-1])