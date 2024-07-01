N=int(input())
arr=[0]
s_arr=[0]
cnt=1
for i in range(N):
    num=int(input())
    if num>arr[-1]:
        cnt+=1
    else:
        cnt=1
    arr.append(num)
    s_arr.append(cnt)

print(max(s_arr))