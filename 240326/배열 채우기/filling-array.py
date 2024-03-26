arr = list(map(int,input().split()))
n = len(arr)

for i in arr[n-2::-1]:
    print(i,end=" ")