a=input()
arr=["apple","banana","grape","blueberry","orange"]
cnt=0
for string in arr:
    if a==string[2] or a==string[3]:
        print(string)
        cnt+=1

print(cnt)