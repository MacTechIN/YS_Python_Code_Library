# print(인자, end='...')
# default(기본값)은 다음 라인으로 이동)
# Line Feed : 라인을 다음 라인으로 이동(Enter)
# ------------------------------------------------
# CRLF : Windows
# LF : Linux, MacOS

print("안녕하세요?")
print("반갑습니다.")

#%%

# 다음 라인으로 이동하지 않고 연속해서 출력
print("안녕하세요?", end=' ') 
print("반갑습니다.", end=' ')
print("환영합니다.")

#%%

t1 = '010'
t2 = '1234'
t3 = '4567'
print(t1, end='-')
print(t2, end='-')
print(t3)

#%%
print("1234567890" * 5)
print("a\tb\tc\t")
print("abcdefg\tb\tc\t")
print("abcd\tb123\tc\t")


#%%
t1 = 'a'
t2 = 'b'
t3 = 'c'
print("1234567890" * 5)
print(t1, end='\t')
print(t2, end='\t')
print(t3)


