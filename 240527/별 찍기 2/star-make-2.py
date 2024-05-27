size,typ=map(int,input().split())

if typ==1:
    num=int((size+1)/2)+1
    num2=size-num
    for i in range(1,num):
        print("*"*i)
    for j in range(num2+1,0,-1):
        print("*"*j)
elif typ==2:
    num=(size+1)//2-1
    for i in range(size):
        if i<num:
            for j in range(num+1):
                if j>=num-i:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        else:
            for j in range(num+1):
                if j>=i-num:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()

elif typ==3:
    for i in range(size):
        for j in range(size):
            if i<=j<=size-i-1 or size-i-1<=j<=i:
                print("*",end="")
            else:
                print(" ",end="")
        print()
else:
    num=(size)//2
    for i in range(size):
        for j in range(size):
            if i<=j<=num or num<=j<=i:
                print("*",end="")
            else:
                print(" ",end="")
        print()