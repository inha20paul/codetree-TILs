n=int(input())
arr=[tuple(input().split()) for _ in range(n)]
arr.sort(key=lambda x: (x[1],x[2],x[3]))
arr=arr[::-1]

for name,korean,eng,math in arr:
    print(name,korean,eng,math)