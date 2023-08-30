# 문자열 바꾸기(replace)
# 문자열에서 바꾸고자 하는 문자열을 찾아서 새로운 문자열로 대체
# 새로운문자열 = 원본문자열.replace(대상문자열, 새로운문자열)
# 원본은 변경되지 않으며 결과를 리턴
# 바뀌는 문자열의 크기가 서로 일치하지 않아도 된다.

a = 'Life is too short!'
b = a.replace('Life', 'Your leg')
print(f"({a}) -> ({b})")

#%%

# 바꾸고자 하는 문자열이 없으면?
# 바뀌지 않은 원본과 동일한 내용을 새로 만들어 준다.
# 대소문자를 구분한다.
c = a.replace('life', 'Your leg')
print(f"바뀌지 않음: ({a}) -> ({c})")

#%%
# [문제]
# 대소문자를 구분하지 않고 바꾸려면?
# String.capitalize() : 첫번째 문자를 대문자로 변환해서 변환된 문자열을 리턴
s = 'life'.capitalize() 
print('s=', s)
c = a.replace(s, 'Your leg')
print(f"({a}) -> ({c})")

