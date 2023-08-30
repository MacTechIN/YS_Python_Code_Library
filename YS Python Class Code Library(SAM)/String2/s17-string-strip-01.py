# 문자열의 양쪽 공백 삭제(strip)
# 양쪽의 모든 공백을 삭제
# 중간에 있는 공백은 유지
# 원본은 변경되지 않으며 결과를 리턴

a = '      Hi!     '
b = a.strip()
print(f'({a}) -> ({b})')

a = '    Hello world!   '
b = a.strip()
print(f'({a}) -> ({b})')



