n=int(input())
arr=[0]*200
for i in range(n):
    x1,x2=map(int,input().split())
    # 0<= x1,x2 <=200 (양수화)
    x1+=100
    x2+=100
    for i in range(x1,x2):
        arr[i]+=1

print(max(arr))