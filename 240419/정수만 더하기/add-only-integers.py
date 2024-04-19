x=input()
sum=0
for i in range(len(x)):
    if x[i].isdigit():
        sum+=int(x[i])

print(sum)