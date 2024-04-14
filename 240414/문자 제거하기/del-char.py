arr=list(input())
lght=len(arr)

for i in range(lght-1):
    num=int(input())
    if num>=len(arr)-1:
        num=len(arr)-1
    arr.pop(num)
    print(''.join(arr))