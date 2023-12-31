# 문자열 포매팅(String Formatting)
# 문자열 포맷 코드
# 정렬, 공백

a = 10
b = 10000
c = 1000
d = 90

# %숫자d : 숫자만큼 자릿수를 확보하여 출력하고 남는 부분은 공백으로 출력
# 정렬: 기본 오른쪽 맞춤
print("[포인트 현황] 오른쪽 정렬")
print("a의 포인트는 (%6d)입니다." %a)
print("b의 포인트는 (%6d)입니다." %b)
print("c의 포인트는 (%6d)입니다." %c)
print("d의 포인트는 (%6d)입니다." %d)

#%%

# 왼쪽정렬 : %-숫자d
print("[포인트 현황] 왼쪽 정렬")
print("a의 포인트는 (%-6d)입니다." %a)
print("b의 포인트는 (%-6d)입니다." %b)
print("c의 포인트는 (%-6d)입니다." %c)
print("d의 포인트는 (%-6d)입니다." %d)

#%%
# 소수점 : 소수점도 전체 자릿수 가운데 포함
pi = 3.14
print("원주율은 (%f)입니다." % pi)          # 기본은 소숫점이하 6자리(3.140000)
print("원주율은 (%10f)입니다." % pi)        # 총 10자리 가운데 나머지는 공백 2자리(  3.140000) 
print("원주율은 (%10.2f)입니다." % pi)      # 총 10자리 소숫점 이하 2자리 나머지는 왼쪽 공백 6자리(      3.14)
print("원주율은 (%-10.2f)입니다." % pi)     # 총 10자리 소수점 이하 2자리 나머지는 오른쪽 공백(3.14      )


#%%
#소숫점 이하 3자리 에서 반올림 하여 표현 
print("원주율은 (%5.2f)입니다." % pi)      # 총 10자리 소숫점 이하 2자리 나머지는 왼쪽 공백 6자리(      3.14)
print("원주율은 (%-20.2f)입니다." % pi)     # 총 10자리 소수점 이하 2자리 나머지는 오른쪽 공백(3.14      )
