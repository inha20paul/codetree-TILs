s,q=input().split()
arr=list(s)

for i in range(int(q)):
    num,a,b=input().split()
    if num=='1':
        arr[int(a)-1],arr[int(b)-1]=arr[int(b)-1],arr[int(a)-1]
        print(''.join(arr))
    elif num=='2':
        for j in range(len(arr)):
            if arr[j]==a:
                arr[j]=b
        print(''.join(arr))