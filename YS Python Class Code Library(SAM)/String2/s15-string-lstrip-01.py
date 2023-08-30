# 문자열의 왼쪽 공백 삭제(lstrip)
# 왼쪽의 모든 공백을 삭제
# 오른쪽이나 중간에 있는 공백은 유지
# 자기 자신은 변경되지 않으며 결과를 리턴
# 왼쪽을 공백을 짤라내라 
# left-strip
a = '      Hi!    '
b = a.lstrip()
print(f'a=({a})')
print(f'b=({b})')

a = '    Hello   world!   '
b = a.lstrip()
print(f'a=({a})')
print(f'b=({b})')
