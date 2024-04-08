n=int(input())
arr=[input() for _ in range(n)]
char=input()
cnt=0
summ=0

for i in range(n):
    if arr[i][0]==char:
        cnt+=1
        summ+=len(arr[i])

avg=summ/cnt

print(cnt,f'{avg:.2f}')