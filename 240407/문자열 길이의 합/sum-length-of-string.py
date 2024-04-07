n=int(input())
arr=[input() for _ in range(n)]
cnt=0
sum_arr=0

for i in range(n):
    if arr[i][0]=='a':
        cnt+=1
    sum_arr+=len(arr[i])

print(sum_arr,cnt)