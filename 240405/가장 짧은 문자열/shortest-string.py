arr=[]
for _ in range(3):
    a=input()
    arr.append(len(a))

print(max(arr)-min(arr))