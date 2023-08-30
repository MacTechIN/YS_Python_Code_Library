# 문자열 포매팅(String Formatting)
# format 함수를 사용한 포매팅
# 포맷문자열.format(값, ...)
# 포맷은 중괄호({순번})로 감싼다.
# 자료형은 알아서 변환을 시킨다.

a = 10
b = 10000
c = 1000
d = 90

print("[포인트 현황]")
print("a의 포인트는 ({0})입니다.".format(a))
print("b의 포인트는 ({0})입니다.".format(b))
print("c의 포인트는 ({0})입니다.".format(c))
print("d의 포인트는 ({0})입니다.".format(d))

