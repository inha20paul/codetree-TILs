string,q=input().split()
arr=list(string)

for i in range(int(q)):
    request=int(input())
    if len(arr)>1:
        if request==1:
            arr=arr[1:]+list(arr[0])
        elif request==2:
            arr=list(arr[-1])+arr[:-1]
        elif request==3:
            arr=arr[::-1]
    print(''.join(arr))