# 문자열 관련 함수
# 결과 = 문자열.함수(...)
# 결과 = 문자열변수.함수(...)

# 문자 개수 세기(count)
# 문자열에서 특정한 문자를 몇 개를 포함하고 있는가?
a = "hobby"
print('count(b) =', a.count('b'))
print('count(x) = ', a.count('x'))

#%%
# 문자열 b에 스페이스(공백)이 몇 개 포함되어 있는가?
b = "welcome to korea"
print(f"{b}.count(' ')={b.count(' ')}")

#%%

tel = "031-123-1234"
telcount = tel.count('-')
print(f"전화번호({tel})는 하이픈이 {telcount}개 포함되어 있습니다.")
#%%
telcount = "031-456-5432".count('-')
print('telcount=', telcount)

#%%
# 숫자는 count() 메소드를 가지고 있지 않음
# SyntaxError: invalid syntax
# numcount = 1007.count('0')
# print('1007=', numcount)

# AttributeError: 'int' object has no attribute 'count'
# num = 1007
# numcount = num.count('0')
# print('1007=', numcount)
#%%
str = "abc,abc,hello,telabcxb,end"
strcount = str.count("ABC") # 0
print('strcount=', strcount)

#%%
strcount = str.count("abc") # 3
print('strcount=', strcount)