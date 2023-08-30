# print() 함수
# format : 문자열로 감싼 형식
# "{0}{1}".format(value0, value1)


hi = "안녕!"
boy = "소년"

print(hi, boy)                      # 안녕! 소년
print(hi, boy, sep=', ')            # 안녕!, 소년
print("{0}, {1}".format(hi, boy))   # 안녕!, 소년
print("{0}-{1}".format(hi, boy))    # 안녕!-소년
print('{0},{1}'.format(hi, boy))    # 안녕!,소년

#%%

# 보기 좋게 편집할 때
print('hi({0}), boy({1})'.format(hi, boy))    # hi(안녕!), boy(소년)
print('hi(', hi, ')', ', boy(', boy, ')', sep='')

#%%

# HTML 
print('<h1>{0}</h1>, <p>{1}</p>'.format(hi, boy))    # <h1>안녕!</h1>, <p>소년</p>
print('<h1>{1}</h1>, <p>{0}</p>'.format(hi, boy))    # <h1>소년</h1>, <p>안녕!</p>
