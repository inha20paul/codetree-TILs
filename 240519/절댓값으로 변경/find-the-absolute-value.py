N=int(input())
arr=list(map(int,input().split()))

def absolute(arr):
    for i in range(N):
        arr[i]=abs(arr[i])

absolute(arr)

for elem in arr:
    print(elem,end=" ")