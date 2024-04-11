A=input()
B=input()
cnt=0

# 탐색범위 = 0~(A크기-B크기)
for i in range(len(A)-len(B)+1):
    if A[i:i+len(B)]==B:
        cnt+=1

print(cnt)