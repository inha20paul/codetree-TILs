n,t=map(int,input().split())
string1="".join(input().split())
string2="".join(input().split())
string3=string1+string2
lght=len(string3)

for i in range(t):
    string3=string3[-1]+string3[:lght-1]

cnt=0
for elem in string3:
    print(elem,end=" ")
    cnt+=1
    if cnt==n:
        print()