N=int(input())
def sum_of_tenpercenct(N):
    sumation=0
    for i in range(1,N+1):
        sumation+=i
    sumation=sumation/10
    return int(sumation)

print(sum_of_tenpercenct(N))