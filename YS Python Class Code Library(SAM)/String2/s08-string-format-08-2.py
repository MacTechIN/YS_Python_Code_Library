# 문자열 포매팅(String Formatting)
# f"문자열"
# f'문자열'

a = 12345
b = "hello"
c = 3.14159

# 포맷에 자료형을 넣을 수 있다.
print(f"    정수: ({a:>10})")
print(f"  문자열: ({b:>10})")
print(f"    실수: ({c:>10})")
print(f"실수포맷: ({c:>10f})")
print(f"실수포맷: ({c:>10.2f})")
print(f"정수포맷: ({a:>10d})")

