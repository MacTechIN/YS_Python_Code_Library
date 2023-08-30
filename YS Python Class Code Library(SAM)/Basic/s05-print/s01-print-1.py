# print() 함수
# 화면에 객체를 출력하는 파이썬의 내장함수(Build-in function)

hi = "Hi!"
boy = "boy"
print(hi,boy) # sep= ' '

print(hi,boy, sep=',') # 콤마

print(hi, boy, sep=', ') # 콤마 + 공백
print(hi, boy, sep='|')  

s1 = "abc"
s2 = "def"
print(s1, end='') # 라인피드(Enter) 키를 없앰
print(s2, end='') # 라인피드(Enter) 키를 없앰
print()

print(s1, s2, sep='') # 분할 문자를 없앰
