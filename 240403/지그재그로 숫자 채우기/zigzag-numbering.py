n,m=map(int,input().split())
arr_2d=[[0]*m for _ in range(n)]
num=0
for i in range(m):
    for j in range(n):
        if i%2==0:
            arr_2d[j][i]+=num
            num+=1
        else:
            arr_2d[n-j-1][i]+=num
            num+=1

for row in arr_2d:
    for elem in row:
        print(elem,end=" ")
    print()