a,b=input().split()
# 두 문자열 리스트에 담기
arr_a=list(a)
arr_b=list(b)
# 리스트 인덱스를 이용해 문자열 교체
arr_b[:2]=arr_a[:2]
# 리스트에 담긴 문자열을 string 타입으로 형변환
ans="".join(arr_b)
# 출력
print(ans)