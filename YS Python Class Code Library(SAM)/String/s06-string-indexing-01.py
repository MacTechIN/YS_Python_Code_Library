# 문자열 인덱싱
# 문자열의 위치를 참조(본다)
# 문자열은 연속된 문자들의 집합
# 시작위치 : 0부터 시작
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0부터 문자열의 길이에서 -1까지, len(문자열) - 1
# 제약사항 : 문자열은 참조는 할 수 있지만 바꿀 수는 없다.

s = "abcdefghijklmnopqrstuvwxyz" # 26자
ln = len(s)
#%%

print('len(s):', ln)  # 문자열의 길이(length)
print('s[0] = ', s[0])  # a
print('s[1] = ', s[1])  # b
print('s[2] = ', s[2])  # c
print('s[25] = ', s[25]) # z
print('s[len(s) - 1] = ', s[len(s) - 1]) # z

#%%
# 바꿀 수 없다(read-only)
# 인덱싱을 통한 참조를 통해서 개별적인 문자를 바꿀 수는 없다.
# TypeError: 'str' object does not support item assignment(할당)
# s[0] = 'A'

s[0] = 'A'


#%%
# 전체 문자열을 바꿀 수는 있다.
# 내부적으로 새로운 메모리에 값을 저장하고 참조하고 있는 주소를 변경
s = "ABC"
print("abc: len({0}) ({1})".format(len(s), s))


