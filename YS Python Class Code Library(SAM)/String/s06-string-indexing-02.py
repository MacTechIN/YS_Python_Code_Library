# 문자열 인덱싱
# 문자열의 위치를 참조
# 시작위치 : 0부터 시작
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0부터 문자열의 길이에서 -1까지
# 제약사항 : 인덱싱을 통한 참조를 통해서 개별적인 문자를 바꿀 수는 없다.

sx = "abcdefghijklmnopqrstuvwxyz"
print('len(sx):', len(sx))  # 문자열의 길이
print('id(sx):', id(sx))    # 객체의 위치, 객체를 식별하는 이름
print(sx[0])  # a
print(sx[1])  # b
print(sx[2])  # c
print(sx[25]) # z
print('id(sx): %x' % id(sx)) #16진수 타입으로 변환

#%%

# 인덱싱을 통한 참조를 통해서 개별적인 문자를 바꿀 수는 없다.
# sx[0] = 'A'

# 전체 문자열을 바꿀 수는 있다.
sx = "ABC"
print('len(sx):', len(sx))  # 문자열의 길이
print('id(sx):', id(sx))    # 객체의 위치, 객체를 식별하는 이름
print(sx)

#%%

num = 10 
print('num(%d) id(%x)' %(num, id(num)))

num = 20 
print('num(%d) id(%x)' %(num, id(num)))


#%%
a = 1 
b = 5

print("a's ID", id(a))
print("b's ID", id(b))


print("")

print("b = a") 
b = a
print("b's ID", id(b))


a = 3 
print("a = 3")
print("a's ID", id(b))


c = 1 
print("c's ID", id(c)) 

d = 1 
print("d's ID", id(d))

e = 3 
print("e's ID", id(e))

c = 3 
print("c's ID", id(c)) 



#%%
y = "Life is too short, You need Python"
print(y[-1])