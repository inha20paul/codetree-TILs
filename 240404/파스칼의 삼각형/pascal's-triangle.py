n=int(input())
arr_2d=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j or j==0:
            arr_2d[i][j]=1

for i in range(n):
    for j in range(n):
        if i>j and j>0:
            arr_2d[i][j]=arr_2d[i-1][j-1]+arr_2d[i-1][j]


for i in range(n):
    for j in range(n):
        if i>=j:
            print(arr_2d[i][j],end=" ")
    print()