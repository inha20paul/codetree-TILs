a,b=map(int,input().split())
num=a+b
string=str(num)
cnt=0
for i in range(len(string)):
    if string[i]=='1':
        cnt+=1

print(cnt)