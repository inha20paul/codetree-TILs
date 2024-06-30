N=int(input())
arr=[]
cnt_arr=[0]*1001
for i in range(N):
    num=int(input())
    arr.append(num)
    if num in arr:
        cnt_arr[num]+=1

if len(arr)==1:
    print(1)
else:
    print(max(cnt_arr)-1)