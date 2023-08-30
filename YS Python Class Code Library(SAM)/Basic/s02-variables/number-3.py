# 자료형 : 숫자형
# 숫자로 이루어진 문자열을 숫자로 변환시켜서 연산을 하려면?

a = 1234    # int
b ='1234'   # str

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# c = a + b
# print(c)

b1 = int(b) # 문자열을 숫자로 변환(숫자형)
print(type(b), b)   # str
print(type(b1), b1) # int
c = a + b1  # 연산이 가능
print(c)