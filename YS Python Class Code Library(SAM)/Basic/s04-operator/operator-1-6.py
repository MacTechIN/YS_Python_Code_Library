# 연산자
# 사칙연산 : +, -, /, *
# 정수나누기 : //
# 몫과 나머지 : divmod(x,y)
# 나머지 : %
# 지수 : **

# divmod(a,b) : 나누다(divide)
# 소숫점을 제외한 몫과 나머지를 튜플(tuple)로 결과를 리턴
# 결과 : 몫(3), 나머지(1)
a = 10
b = 3
g = divmod(a, b)
print('a=', a)
print('b=', b)
print('g=divmod(a,b) :g=', g)
print('몫 : ', g[0])
print('나머지 : ', g[1])

