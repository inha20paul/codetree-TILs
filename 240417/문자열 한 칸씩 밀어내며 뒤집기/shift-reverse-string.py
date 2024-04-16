string,q=input().split()
lgth=len(string)
s=''
for i in range(int(q)):
    request=int(input())
    if lgth>1:
        if request==1:
            string=string[1:]+string[0]
            print(string)
        elif request==2:
            string=string[-1]+string[:-1]
            print(string)
        elif request==3:
            for j in range(len(string)):
                s=s+string[-j-1]
            string=s
            print(string)
    else:
        print(string)