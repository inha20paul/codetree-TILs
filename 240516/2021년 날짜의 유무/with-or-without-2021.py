# 월,일
# 2월은 28일까지
M,D=map(int,input().split())

def IsMD(M,D):
    arr31=[1,3,5,7,8,10,12]
    if M in arr31:
        return 1<=D<=31
    elif M==2: # D는 28일까지
        return 1<=D<=28
    else: # 30일까지
        return 1<=D<=30

if IsMD(M,D):
    print("Yes")
else:
    print("No")