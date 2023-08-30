# 변수(Variable)
# 1. 메모리의 위치를 나타내는 별칭
# 2. 종류: 자료형별로 구별(문자형, 숫자)

# 변수(variable) : 메모리 영역(주소)의 별칭
# 메모리 주소는 2진수로 되어 있으며 8비트(1바이트) 단위로 구성
# 변수를 선언하게 되면 메모리의 영역을 할당한다.

# 변수를 선언하는 명명규칙(이름을 만드는 규칙)
# 소문자(a~z)
# 대문자(A~Z)
# 숫자(0~9)
# 특수문자: 언더스코어(_)
# 제약조건(예외사항)
#   -> 숫자로 시작할 수 없다.
#   -> 영문자나 언더스코어로 시작해야 한다.
#   -> 예약어(reserved word, key-word)를 사용할 수 없다.

# 예약어
# assert = 10

# 대소문자 구분이 된다.
Assert = 10
print('Assert=', Assert)

#%%

a = 10  # 최초에는 a는 변수가 선언되어 있지 않은 상태
a = 20  # 기존에 있던 값 10은 사라지고 20이 들어간다.
print('a=', a)

#%%
<<<<<<< HEAD

=======
>>>>>>> origin/master
# x와 y의 값을 바꾸려면?
x = 77
y = 88
print('x=', x)
print('y=', y)

#%%
y = x # y = 77
x = y # x = y(77)
print('x=', x)
print('y=', y)

#%%
print('x와 y값의 교환')
z = x   # x값을 z에 임시보관(대피)
x = y
y = z
print('x=', x)
print('y=', y)

#%%

<<<<<<< HEAD

=======
>>>>>>> origin/master
print('x와 y값의 재교환(원상복구)')
x, y = y, x
print('x=', x)
print('y=', y)

#%%
# 튜플
a = 10
b = 20
e = 30
m = a, b, e
x, y, z = m   # unpacking, tuple -> x, y
c, d = a, b # unpacking, tuple -> c, d
print(x, y, z)
print(c, d)

#%%

x = m[0]
y = m[1]
print(x, y)

