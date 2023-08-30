# 문자열 연산자
# 덧셈, 곱셈

# 문자열 덧셈
# 문자열에서 덧셈(+)은 문자열을 붙인다.
s1 = "안녕"
s2 = "하세요"
s3 = s1 + s2
print(s1 + s2)
print(s1, s2, sep='')
print(s3)

<<<<<<< HEAD
print(s1,s2)
print(s1,s2, sep="")


=======
>>>>>>> origin/master
#%%

# 문자열 곱셈
# 문자열 곱셈은 해당 문자열을 지정된 회수 만큼 반복해서 붙인다.
s4 = '*' * 10
print("12345678901234567890")
print(s4)
print('#' * 10)

#%%
s5 = "12345-" * 10
print(s5)

<<<<<<< HEAD

#%%
# 다항식으로 쓸경우 어떻게 될까?

s5 = ("124" * 10) +  ('-' * 10)

s6 = "124" * 10 * 3

print(s6)
 
=======
#%%
# TypeError: can't multiply sequence by non-int of type 'str'
# s6 = "123" * 10 * '-' * 1


#%%
s6 = "123" * 10 + '-' * 1
print(s6)

#%%
s7 = "123" * 10 * 5
print(s7)


>>>>>>> origin/master
