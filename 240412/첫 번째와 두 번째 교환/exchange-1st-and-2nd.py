a=input()
arr=list(a)
a1=a[0]
a2=a[1]
for i in range(len(a)):
    if arr[i]==a1:
        arr[i]=a2
    elif arr[i]==a2:
        arr[i]=a1
ans=''.join(arr)
print(ans)