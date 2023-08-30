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

print("현재 온도는 (%d)도 입니다." % num)

#%%

numformat = "2 %d %d %d" % (num,num, num*num)
print(numformat)