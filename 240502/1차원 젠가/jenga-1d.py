n=int(input())
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

for i in range(2):
    a,b=map(int,input().split())
    temp_arr=arr[0:a-1]+arr[b:]
    arr=temp_arr

print(len(arr))
for elem in arr:
    print(elem)