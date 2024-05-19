N=int(input())
arr=list(map(int,input().split()))

def f (arr):
    for i in range(N):
        if arr[i]%2==0:
            arr[i]=int(arr[i]/2)

def printArr(arr):
    for elem in arr:
        print(elem,end=" ")


f(arr)
printArr(arr)