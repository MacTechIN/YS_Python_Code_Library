# 문자열 위치 검색(index)
# 찾는 문자열이 없으면 프로그램이 종료

#    0123456789012345678901234
a = "Python is the best choice"

# 찾는 문자열을 어떻게 연속해서 찾을 있는가?
# 문자열.index(검색문자열, 시작위치)
# string.index(findstring, startindex)
print(f"문자열({a})에서 문자('t')의 위치를 검색(index)")
tcnt1 = a.index('t')
print('tcnt1=', tcnt1)

#%%

tcnt2 = a.index('t', tcnt1 + 1)
print('tcnt2=', tcnt2)

# Error : 프로그램이 종료
# ValueError: substring not found
tcnt3 = a.index('x', tcnt2 + 1)
print('tcnt3=', tcnt3)

print('THE END')