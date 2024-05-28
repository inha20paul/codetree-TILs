n=int(input())
arr=[tuple(input().split()) for _ in range(n)]
arr.sort(key=lambda x:x[1]) #키를기준 : x[1]

for name,h,w in arr:
    print(name,h,w)