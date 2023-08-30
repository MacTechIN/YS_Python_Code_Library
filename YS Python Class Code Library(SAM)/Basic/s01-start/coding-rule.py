# 코딩 규칙

# 변수(variable) : 메모리 영역(주소)의 별칭
# 메모리 주소는 2진수로 되어 있으며 8비트(1바이트) 단위로 구성
# 변수 a를 선언하게 되면 메모리의 영역을 할당한다.

# 변수를 선언하는데 초깃값을 지정하지 않으면?
# NameError: name 'abc' is not defined.
# abc

# 변수는 초깃값을 지정해야 한다.


# 변수 = 초깃값
x = 10      # x <- 10, x에 값 10을 넣어라
y = 256     # y <- 10, y에 값 256을 넣어라
print(x)
print(y)

# 한글로 변수를 선언 가능
홍길동 = 100000
전우치 = '나의 이름은 전우치'
양귀비 = '나는 양귀비입니다.'  
양귀비 = 전우치  # 원래의 값은 사라진다. 전우치의 내용은 유지된다.
홍길동 = '고대 사람'
print(홍길동)
print(전우치)
print(양귀비)

# 변수를 선언하는 명명규칙(이름을 만드는 규칙)
# 소문자(a~z)
# 대문자(A~Z)
# 숫자(0~9)
# 특수문자: 언더스코어(_) : 키보드(Shift-)
# 제약조건(예외사항)
#   -> 숫자로 시작할 수 없다.
#   -> 영문자나 언더스코어로 시작해야 한다.
#   -> 예약어(reserved word, key-word)를 사용할 수 없다.

# [Reserved Word]
"""
False, class, finally, is, return, None, continue,
for, lambda, try, True, def, from, nonlocal, while
and, del, global, not, with, as, elif, if, or, yield
assert, else, import, pass, break, except, raise
"""

xy = 10
XY = 20
Msg = "소식"
_Hello = "Hi!"
A123 = "A123"
print(xy, XY, Msg, _Hello, A123)

# SyntaxError: invalid syntax
# $Dal = 10

# SyntaxError: invalid syntax
# 9abc = 99

# SyntaxError: can't assign to keyword
# False = "False"

# 변수를 선언하고 값을 지정하지 않으면?

# NameError: name 'Welcome' is not defined
# 변수를 선언할 때 반드시 초기값을 지정해야 한다.
# 변수가 초깃값을 지정하여 변수의 자료형을 갖게된다.
# Welcome

# 자료형
# 정수, 실수, 문자열, 논리형, 객체

# 들여쓰기(indent)
# 원래 Tab은 기본적으로 8칸이다.
# 코드 블럭은 일반적으로 Tab(4칸) 단위로 들여쓰기를 한다.
# 같은 블럭에서 들여쓰기 간격을 같아야 한다.
# 탭(Tab), 스페이스(Space)를 혼용해서는 않는다.(혼용해도 오류가 나지는 않는다)

s = '''
다중 라인 문자열
(multi-line comment)
'''

print(s)

"""
멀티라인 주석
01234567890
대분류
    중분류
        소분류1
        소분류2

"""        

# 세미콜론(;)
# 문장의 끝에 붙인다.
# 일반적으로 생략한다.
# 여러 명령문을 하나의 라인에 기술할 때 세미콜론을 붙여서 쓸 수 있다.
print('hello, python, ');   # 명시적으로 문장의 끝을 세미콜론으로 표시할 수 있다.
print('welcome to korea!')  # 자동으로 붙여서 처리를 해 준다.

# 하나의 라인으로 연속해서 기술할 수 있다.
# 반드시 문장을 구분하기 위해서 세미콜론을 붙여야 한다.
print('hello, python, '); print('welcome to korea!')
