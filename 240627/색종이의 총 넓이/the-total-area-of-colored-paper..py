N=int(input())
arr=[[0]*200 for _ in range(200)]

for i in range(N):
    r,c=map(int,input().split())
    r+=100
    c+=100
    for j in range(8):
        for k in range(8):
            arr[r+j][c+k]=1

s=0

for row in arr:
    for elem in row:
        s+=elem

print(s)