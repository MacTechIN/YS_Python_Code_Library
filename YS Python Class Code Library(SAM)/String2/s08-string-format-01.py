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

# 정수(%d) : decimal
# numformat = "현재 온도는 (30)도 입니다."
num = 30
numformat = "현재 온도는 (%d)도 입니다." % num
print(numformat)

# 문자열(%s)
name = "홍길동"
strformat = "오늘의 당직자는 (%s)님 입니다." % name
print(strformat)

# 문자열과 정수를 복합적으로 써서 문자열 포매팅에 적용할 때
# 대응되는 값 또는 리스트는 괄호로 묶어야 한다.
# 문자(%c) : Character, Integer
# 문자는 하나의 글자 : a, b, c, 한, 글, 1, 2, 3, 4
# 문자열: TypeError: %c requires int or char
# ch = 'abc'

ch1 = 65 # 영문자는 ASCII, 대문자('A')
ch2 = 'A'
ch3 = 'a'
ch4 = 97 # 'a'
print("문자 포맷 테스트: (%c)(%c)(%c)(%c)는 하나의 문자입니다." % (ch1, ch2, ch3, ch4))
print("문자 포맷 테스트: (0x%x)(0x%x)는 하나의 문자입니다." % (ch1, ch4)) # 0x41, 0x61

# Literal % : 문자 자체(%)를 출력하기 위해서는 연속해서 두 번('%%')
# print("오늘의 비가 올 확률은 (%d)% 입니다." % 45)
print("오늘의 비가 올 확률은 (%d)%% 입니다." % 45)

# 부동 소숫점(%f) : float
eco = 3.45
print("올해의 한국 경제 성장율 예상치는 (%d) 입니다." % eco) # 결과: 3
print("올해의 한국 경제 성장율 예상치는 (%f) 입니다." % eco) # 결과: 3.450000


