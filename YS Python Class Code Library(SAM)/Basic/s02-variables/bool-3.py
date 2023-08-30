# bool
# True 또는 False 값을 가질 수 있다.

# 크기비교
# 크다 : >
# 작다 : <
# 크거나 같다 : >=
# 작거나 같다 : <=
# 결과는 bool 자료형

#%%
a = (1 > 2)
b = (1 < 2)
c = (True > False) # 1 > 0
d = (True < False) # 1 < 0

print('a:', a, type(a)) # False
print('b:', b, type(b)) # True
print('c:', c, type(c)) # True
print('d:', d, type(d)) # False

#%%

gt = (10 > 10)

ge1 = (10 >= 10)
ge2 = (10 > 10) or (10 == 10)
ge3 = (ge1 == ge2)

lt = (10 < 10)

le1 = (10 <= 10)
le2 = (10 < 10) or (10 == 10)

