# 문자열의 오른쪽 공백 삭제(rstrip)
# 오른쪽의 모든 공백을 삭제
# 왼쪽이나 중간에 있는 공백은 유지
# 원본은 변경되지 않으며 결과를 리턴

# right strip
a = '      Hi!     '
b = a.rstrip()
print(f'({a}) -> ({b})')
print()

a = '    Hello world!    '
b = a.rstrip()
print(f'({a}) -> ({b})')
