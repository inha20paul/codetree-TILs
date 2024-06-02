n=int(input())
arr=[0]*100
for i in range(n):
    x1,x2=map(int,input().split())
    for j in range(x1-1,x2):
        arr[j]+=1

print(max(arr))