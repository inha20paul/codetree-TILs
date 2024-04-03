n=int(input())
size=n*n
arr_2d=[[0]*n for _ in range(n)]
col=n-1
row=n-1

for num in range(1,size+1):
    arr_2d[row][col]=num
    if col%2==(n-1)%2:
        if 0<=row-1<n:
            row-=1
        else:
            col-=1
    else:
        if 0<=row+1<n:
            row+=1
        else:
            col-=1

for row in arr_2d:
    for elem in row:
        print(elem,end=" ")
    print()