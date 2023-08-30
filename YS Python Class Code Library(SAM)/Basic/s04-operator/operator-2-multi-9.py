# 복합 대입연산자(축약형)
# **= : 지수(거듭제곱)을 해서 대립

a = 3
b = 10
print('a=', a)
print('b=', b)

b **= a
print('b=', b) # 1000

# **= : 지수(거듭제곱)을 해서 대립 : b = b ** a
b = 2
a = 3
b **= a 
print('a=', a) # 8
print('b=', b)
print('b **= a : ', b)
