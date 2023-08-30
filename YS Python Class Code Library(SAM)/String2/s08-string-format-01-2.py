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


# 문자열(%s)
name = "홍길동"
strformat = "오늘의 당직자는 (%s)님 입니다." % name
print(strformat)


