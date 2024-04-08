arr=[input() for _ in range(10)]
char=input()

for i in range(10):
    if arr[i][-1]==char:
        print(arr[i])