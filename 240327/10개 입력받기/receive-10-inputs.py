arr = list(map(int,input().split()))
sum=0
cnt=0

for i in arr:
    if i==0:
        break
    else:
        sum+=i
        cnt+=1

avg=sum/cnt

print(f'{avg:.1f}')