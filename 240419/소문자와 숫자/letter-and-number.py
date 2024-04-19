x=input()
lgth=len(x)
# 영문자와 숫자만 출력
# 영문자일때 소문자로 .lower()

for i in range(lgth):
    if x[i].isalpha():
        print(x[i].lower(),end="")
    elif x[i].isdigit():
        print(x[i],end="")