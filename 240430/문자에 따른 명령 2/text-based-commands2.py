string=input()


#시작위치
x,y=0,0

# 시작방향=북
dir_num=0
# 북,동,남,서
dx=[0,1,0,-1]
dy=[1,0,-1,0]

for i in string:
    # 반시계 회전
    if i=='L':
        dir_num=(dir_num-1)%4
    # 시계방향 회전
    elif i=='R':
        dir_num=(dir_num+1)%4
    # 전진
    elif i=='F':
        x+=dx[dir_num]
        y+=dy[dir_num]

print(x,y)