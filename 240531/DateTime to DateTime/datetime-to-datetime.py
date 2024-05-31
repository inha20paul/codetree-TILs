# 일,시,분
a,b,c=map(int,input().split())

def countMinute(d,h,m):
    h+=d*24
    m+=h*60
    return m

start=countMinute(11,11,11)
end=countMinute(a,b,c)

if start>end:
    print(-1)
else:
    print(end-start)