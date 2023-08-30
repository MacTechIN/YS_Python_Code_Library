# 문자열 포매팅(String Formatting)
# 문자열 포맷 코드
# %s : 문자열(string)
# %c : 문자 1개(character)
# %d : 정수(decimal)
# %f : 실수,부동소수(float)
# %o : 8진수(octal)
# %x : 16진수(hexa-decimal)
#
# 포맷문자열 % 변수
# 포맷문자열 % (변수, ...)


# 문자열과 정수를 복합적으로 써서 문자열 포매팅에 적용할 때
# 대응되는 값 또는 리스트는 괄호로 묶어야 한다.
today = "2021-12-28"
temp = -3
msg = "오늘의 날짜는 (%s)이며, 온도는 (%d)도 입니다." % (today, temp)
print(msg)

