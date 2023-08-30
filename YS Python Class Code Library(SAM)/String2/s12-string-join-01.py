# 문자열 삽입(join)

# 새로운 문자열 = 삽입할문자열.join(원본문자열)
# 원본문자열에 각 문자들 사이에 문자열을 삽입한다.

# 문자열에 콤바를 삽입하여 새로운 문자열을 생성하여 리턴

s1 = ','.join('abcdefg')
print('s1=', s1)
#%%






#%%

# 원본 문자열을 변경하지 않음
s2 = 'hello'
s3 = ','.join(s2)
print('s2:', s2)
print('s3:', s3)

# 한글
s2 = '헬로우(hello)'
s3 = ','.join(s2)
print('s2:', s2)
print('s3:', s3)
