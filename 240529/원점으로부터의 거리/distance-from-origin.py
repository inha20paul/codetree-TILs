N=int(input())
arr=[]
for i in range(1,N+1):
    x,y=map(int,input().split())
    arr.append((i,abs(x)+abs(y)))

arr.sort(key=lambda x:x[1])
for index,_ in arr:
    print(index)