N=int(input())
arr=list(map(int,input().split()))
arr_origin=[elem for elem in arr] # sort후에도 변하지 않게 직접 할당
arr.sort()

for elem in arr_origin:
    idx=arr.index(elem)
    arr[idx]=-1
    print(idx+1,end=" ")