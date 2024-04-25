n,m=map(int,input().split())

def maximum_(n,m):
    num=1
    while True:
        if num%n==0 and num%m==0:
            print(num)
            break
        else:
            num+=1

maximum_(n,m)