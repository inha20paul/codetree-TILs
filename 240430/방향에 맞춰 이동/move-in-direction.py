# N번 이동
N=int(input())

#시작위치
x,y=0,0

# 동,서,남,북
dx=[1,-1,0,0]
dy=[0,0,-1,1]

#방향 (0:동, 1:서, 2:남, 3:북)
dir_num=0

for i in range(N):
    way,num=input().split()
    num=int(num)
    # 방향을 dirnum으로 변환
    if way=='E':
        dir_num=0
    elif way=='W':
        dir_num=1
    elif way=="S":
        dir_num=2
    else:
        dir_num=3
    # dx,dy 방향 num 만큼 이동
    x,y=x+dx[dir_num]*num,y+dy[dir_num]*num

print(x,y)