# 소문자를 대문자로 변환(upper)

# 문자열을 대문자로 변환하여 새로운 문자열을 리턴
# 기존 문자열은 변경되지 않는다.
# 변수 = 문자열.upper()
a = 'hi'
A = a.upper()
print('a=', a)
print('A=', A)

print('대문자(ABC)를 upper로 변환하면?', 'ABC'.upper())

# 대문자.upper()
good = "GOOD!"
print("good.uppder() ->", good.upper())

# 대소문자 섞여있는 경우 사용]
Hello = "Hello!"
print(Hello, "->", Hello.upper())

# 한글과 같이 영문이 아닌 경우는 있는 그대로 출력
Hangeul = "한글과 English"
print(Hangeul, "->", Hangeul.upper())
