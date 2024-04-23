N=int(input())

def squre(N):
    num=0
    for i in range(N):
        for j in range(N):
            num+=1
            if num>9:
                num=1
            print(num,end=" ")
        print()

squre(N)