# 자료형(데이터 형태)
# 숫자형 : 연산을 수행할 수 있는 형태의 데이터
# 정수: 0, 1234, -1234, 소숫점이 없는 값(유리수)
# 실수: 소수점이 있는 값
#
# 숫자를 표현하는 형태
# 10진수(decimal) : 123456, 3.14
# 2진수(binary)   : 10101100
# 8진수(octal)    : 0o377(0xff, 255), 0O245
# 16진수(hexa-decimal): 0xFF(255), 0xffff(65535), 0x1234

# 10진수 : 10
# 16진수 : 0xA
# 2진수  : 1010
# 8진수  : 0o12

# 정수(int) : integer 약자로 int
# 정수형은 길이의 제한이 없다.
# 컴퓨터가 수용할 수 있는 한계까지 표현이 가능
n1 = 1234567890
print('10자리 정수:', n1)

n2 = 12345678901234567890
print('20자리 정수:', n2)

n3 = 1234567890123456789012345678901234567890
print('40자리 정수:', n3)

n4 = 12345678901234567890
n5 = n4 + 1 
print('20자리 정수:', n4)
print('20자리 정수에 1일 더함:', n5)

n6 = n3 + 17
print('40자리 연산:', n6)

#%%
b64 = 2 ** 64
print("2의 64승?")
print("1234567890" * 3)
print(b64)
print(int(b64 / 1000), "킬로(KB)")
print(int(b64 / (1000 * 1000)), "메가(MB)")
print(int((b64 / (1000000 * 1000))), "기가(GB)")
print(int((b64 / (1000000 * 1000 * 1000))), "테라(TB)")

print(int((b64 / (1000000 * 1000 * 1000) * 200)), "영화편")


