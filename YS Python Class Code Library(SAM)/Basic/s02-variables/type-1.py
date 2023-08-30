# type
# 자료형을 검사
# 자료형에 대한 정보 제공

print(type(1234))   # 정수형(int)
print(type(3.14))   # 실수형(float)
print(type("abc"))  # 문자형(str)

# 논리형(bool): 참, 거짓
print(type(True))   # 논리형(bool)
print(type(False))  # 논리형(bool)

# 정수형을 논리형으로 변환
# int -> bool
print('# bool')
print('bool(1) = ', bool(1))
print('bool(0) = ', bool(0))

# 논리형을 정수형로 변환
# bool -> int
print('# int')
print('int(True) = ', int(True))
print('int(False) = ', int(False))
 
# 문자열을 실수형으로 변환
# str -> float
s1 = '0.1234'
s2 = '3.14e3'
s3 = '3.0e3'
print(float(s1), type(float(s1)))

x1 = float(s1)
t1 = type(x1)
print(t1)


print(float(s2), type(float(s2)))
print(float(s3), type(float(s3)))



