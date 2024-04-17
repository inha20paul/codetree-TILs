A=input()
ascii=ord(A)
# a-z 의 ascii_code값 97-122 

# a일때 z로 할당
if ascii==97:
    ascii=122
# 그 외 이전문자 할당
else:
    ascii-=1
# 아스키 코드를 문자열로 변환 후 출력
print(chr(ascii))