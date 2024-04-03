n,m=map(int,input().split())
arr_2d=[[0]*m for _ in range(n)]
size=n*m
i,j=0,0
cnt_col=0
cnt_row=0

for num in range(1,size+1):
    arr_2d[i][j]+=num
    if 0<=i+1<n and 0<=j-1<m:
        i+=1
        j-=1
    else:
        if cnt_col<m-1:
            cnt_col+=1
            i=0
            j=cnt_col
        else:
            cnt_row+=1
            i=cnt_row
            j=m-1

    
for row in arr_2d:
    for elem in row:
        print(elem,end=" ")
    print()