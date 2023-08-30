# bool
# True 또는 False 값을 가질 수 있다.

# 같다 : ==

# 결과는 bool 자료형
a = "홍길동"
b = "전우치"

c = (a == b)
d = (a is b)

e = (a != b)
f = (not a is b)

print('a:', a, type(a)) # False
print('b:', b, type(b)) # True

print('c:', c, type(c)) # False
print('d:', d, type(d)) # False
print('e:', e, type(e)) # True
print('f:', e, type(e)) # True
