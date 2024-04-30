N=int(input())
x,y=0,0
dx=[1,-1,0,0]
dy=[0,0,-1,1]
dir_num=0
for i in range(N):
    way,num=input().split()
    num=int(num)
    if way=='E':
        dir_num=0
    elif way=='W':
        dir_num=1
    elif way=="S":
        dir_num=2
    else:
        dir_num=3
    x,y=x+dx[dir_num]*num,y+dy[dir_num]*num

print(x,y)