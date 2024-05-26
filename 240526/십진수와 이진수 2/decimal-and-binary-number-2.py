N=input()
N=N[::-1]
deci=0
for i in range(len(N)):
    deci+=(2**i)*int(N[i])

deci*=17

ans=[]

while True:
    if deci<2:
        ans.append(deci)
        break
    ans.append(deci%2)
    deci=deci//2

ans=ans[::-1]

for elem in ans:
    print(elem,end="")