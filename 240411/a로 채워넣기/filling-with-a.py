a=list(input())
# 2번째 원소, 뒤에서 2번째 원소를 'a'로 대체!
a[1],a[-2]='a','a'
b=''.join(a)
print(b)