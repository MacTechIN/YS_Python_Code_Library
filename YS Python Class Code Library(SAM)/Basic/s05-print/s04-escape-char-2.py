# escape character
# 백슬래시(\) 기호를 사용

<<<<<<< HEAD
# 인용부호 : "안녕"
# \" : 쌍따옴표를 출력할 문자로 처리
msg = "영희는 철수에게 \"안녕\"이라고 말했다."

#msg = "영희는 철수에게 "안녕"이라고 말했다." <- 오류 발표 

print(msg)
#%%


# 백슬래시(\)를 출력을 하려고 할 때
msg = "영희는 철수에게 \안녕\이라고 말했다."
print(msg)
=======
#%%
# 인용부호 : "안녕"
# \" : 쌍따옴표를 출력할 문자로 처리
msg = "영희는 철수에게 \"안녕\"이라고 말했다."
print(msg)

#%%
msg = '영희는 철수에게 "안녕" 이라고 말했다.'
print(msg)

#%%
msg = "영희는 철수에게 '안녕' 이라고 말했다."
print(msg)

#%%
# 백슬래시(\)를 출력을 하려고 할 때
msg = "영희는 철수에게 \안녕\이라고 말했다."
print(msg)

>>>>>>> origin/master
#%%

# \\ : 백슬래시(\)를 출력을 하려고 할 때 연속해서 두 번 기술
msg = "He is always saying \\Could you say is again?\\"
print(msg)

#%%
<<<<<<< HEAD

=======
>>>>>>> origin/master
# raw string(이스케이스 문자 무시) 
# 문자열 앞에 r"...."
# \\ : 그대로 출력
print(r"He is always saying \\Could you say is again?\\")

<<<<<<< HEAD
#%%

msg = r"He is always saying \nCould you say is again?\\"
print(msg)

#%%


str = "인사말 : {{{0}}}! {{{1}}}님, 안녕하세요"

print(str.format("안녕", "누구야"))

print(r"{}{}{}{}{}}}{{{}}")
print(r"m""s""g")
=======
msg = r"He is always saying \nCould you say is again?\\"
print(msg)

>>>>>>> origin/master
