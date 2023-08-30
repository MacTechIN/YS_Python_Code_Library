# 문자열 위치 검색(find)
# 처음 만나는 문자열을 찾음
# 찾는 문자열일 없으면 : 리턴 -1

#    0123456789012345678901234
a = "Python is the best choice"
a1 = a.find('i')
a2 = a.find('k')
print('i=', a1) # result = 7
print('f=', a2)
#%%

# 찾지 못하면 -1을 리턴
print('k=', a2) # result = -1

print('is=', a.find("is"))
#%%

# 찾는 문자열에서 최초에 찾은 위치를 리턴
print('t=', a.find("t"))
#%%

# 찾는 문자열을 어떻게 연속해서 찾을 있는가?
# slicing
# 0123456789012345678901234
# Python is the best choice


tcnt1 = a.find('t')
print(f"1st tcntl :{tcnt1} " )
print('tcnt1=', tcnt1)

tstr = a[tcnt1+1:]
print(tstr)

tcnt2 = tstr.find('t')

print('tcnt1=', tcnt2)
print('tcnt2=', tcnt1 + tcnt2 + 1)



