N=int(input())

arr=[[0]*200 for _ in range(200)]

for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            arr[j][k]=1

size=0

for row in arr:
    for elem in row:
        size+=elem

print(size)