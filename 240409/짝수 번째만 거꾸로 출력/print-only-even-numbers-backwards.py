a=input()
lgth=len(a)

for i in range(lgth-1,-1,-1):
    if i%2==1:
        print(a[i],end="")