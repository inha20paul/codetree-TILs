# 키 작은순, 무게 큰 순
N=int(input())
arr=[]

for i in range(N):
    h,w=map(int,input().split())
    arr.append((h,w,i+1))

arr.sort(key=lambda x:(x[0],-x[1]))

for h,w,idx in arr:
    print(h,w,idx)