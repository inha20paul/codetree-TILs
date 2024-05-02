n,t=map(int,input().split())
string1="".join(input().split())
string2="".join(input().split())
string3="".join(input().split())
string_T=string1+string2+string3
lgth=len(string_T)

for _ in range(t):
    string_T=string_T[-1]+string_T[:lgth-1]

cnt=0

for elem in string_T:
    print(elem,end=" ")
    cnt+=1
    if cnt%n==0:
        print()