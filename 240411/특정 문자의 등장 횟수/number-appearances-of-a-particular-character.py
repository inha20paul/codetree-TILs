a=input()
char1="ee"
char2="eb"
cnt1=0
cnt2=0
lgth=len(a)

for i in range(lgth-len(char1)+1):
    if a[i:i+2]=='ee':
        cnt1+=1
    elif a[i:i+2]=='eb':
        cnt2+=1

print(cnt1,cnt2)