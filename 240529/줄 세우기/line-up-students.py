N=int(input())
# 키,몸무게,인덱스
stud=[]
for i in range(1,N+1):
    h,w=map(int,input().split())
    stud.append((h,w,i))

stud.sort(key=lambda x:(-x[0],-x[1],x[2]))
for h,w,i in stud:
    print(h,w,i)