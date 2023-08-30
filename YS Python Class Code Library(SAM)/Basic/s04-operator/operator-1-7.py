# 연산자
# 사칙연산 : +, -, /, *
# 정수나누기 : //
# 나머지 : %, divmod(x,y)
# 지수 : **


# 나머지 : % 
# a를 b로 나눠서 나머지를 취함
a = 10
b = 3
c = a % b
print('a=', a)
print('b=', b)
print('c=', c)

#%%

<<<<<<< HEAD
#[문제]
#나머지 연산자 없이 나머지 구하기 
a = 10 
b = 3 

r1 = 10//3 
print(r1)

r2  = a-(b * r1)
print(r2) 

print("remain :" , r2 )

#%%

a= 16
b = 3 

print('a/b')

r1 = a//b
r2  = a -(b * r1)
print("몫: " ,r1) 
print("remain :" , r2 )


#%%

m = a -( b * (a//b))

print(m)

#%%
=======
# [문제]
# 나머지 연산자(%)나 divmode() 함수를 사용하지 않고 나머지를 구하라.

m = a // b      # 몫
n = a - (m * b) # 나머지
print(m, n)

#%%

m = int(a / b)
n = a - (m * b) # 나머지
print(m, n)

#%%
print(a - a // b * b)
print(a - (a // b * b))

#%%

print(a - int(a / b) * b)



>>>>>>> origin/master

