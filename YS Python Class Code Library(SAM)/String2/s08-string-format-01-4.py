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


# 문자(%c) : Character, Integer
# 문자는 하나의 글자 : a, b, c, 한, 글, 1, 2, 3, 4

#%%
# 문자열: TypeError: %c requires int or char

ch = 'abc'

print("문자열을 문자로 출력 하면 (%c)" % ch)
print("문자열을 문자로 출력 하면 (%s)" % ch)

#%%
ch1 = 65 # 영문자는 ASCII, 대문자('A')

ch2 = 'A'

print(type(ch1))
print(type(ch2))

print (" ASCII Code (%d)는 (%c) 입니다." % (65, 65))

#%%

ch3 = 'a'
ch4 = 97 # 'a'
print("문자 포맷 테스트: (%c)(%c)(%c)(%c)는 하나의 문자입니다." % (ch1, ch2, ch3, ch4))
print("문자 포맷 테스트: (0x%x)(0x%x)는 하나의 문자입니다." % (ch1, ch4)) # 0x41, 0x61

#%%
# Literal % : 문자 자체(%)를 출력하기 위해서는 연속해서 두 번('%%')
# print("오늘의 비가 올 확률은 (%d)% 입니다." % 45)
print("오늘의 비가 올 확률은 (%d)%% 입니다." % 45)


