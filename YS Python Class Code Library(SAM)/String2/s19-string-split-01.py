# 문자열 나누기(split)
# 문자열을 공백 기준으로 나누고 리스트화 시켜줌 

# 기본: 공백을 기준으로 문자열을 분할하여 배열(list)형으로 리턴
# 배열: 연속된 값들의 모임
a = 'Life is too short'
b = a.split()
print(a)
print(b) # ['Life', 'is', 'too', 'short']

print(b[0])
print(b[1])
print(b[2])
print(b[3])

# 결과를 다시 문자열로 변환
c = ' '.join(b)
print(c)