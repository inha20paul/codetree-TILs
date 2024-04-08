n=int(input())
arr=list(input().split())
ans=''.join(arr)
cnt=0
for elem in ans:
    print(elem,end="")
    cnt+=1
    if cnt==5:
        print()
        cnt=0