Y,M,D=map(int,input().split())

def isYoonYear(Y):
    if Y%4==0:
        if Y%400==0:
            return True
        elif Y%100==0:
            return False
        else:
            return True
    else:
        return False

def isInDate(Y,M,D):
    arr31=[1,3,5,7,8,10,12]
    if M in arr31:
        return 1<=D<=31
    elif M==2:
        if isYoonYear(Y):
            return 1<=D<=29
        else:
            return 1<=D<=28
    else:
        return 1<=D<=30


def whatWeather(Y,M,D):
    if isInDate(Y,M,D):
        if 3<=M<=5:
            print("Spring")
        elif 6<=M<=8:
            print("Summer")
        elif 9<=M<=11:
            print("Fall")
        else:
            print("Winter")

whatWeather(Y,M,D)