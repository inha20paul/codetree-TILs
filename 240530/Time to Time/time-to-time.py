# a,b,c,d=map(int,input().split())
# start=(60*a)+b
# end=(60*c)+d

# print(end-start)

a,b,c,d=map(int,input().split())
cnt=0

while True:
    if a==c and b==d:
        break
    cnt+=1
    b+=1
    if b==60:
        a+=1
        b=0

print(cnt)