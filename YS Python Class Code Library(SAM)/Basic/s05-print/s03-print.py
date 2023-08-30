# print() 함수
# format : 문자열로 감싼 형식
# "{0}{1}".format(value0, value1)

<<<<<<< HEAD

fmt = "인사말 : {0}?  {1}님, 반갑습니다."

hi = "안녕!"
=======
fmt = "인사말 : {0}! {1}님. 반갑습니다."
hi = "안녕"
>>>>>>> origin/master
boy = "철수"

#%%

print(fmt.format(hi, boy))
<<<<<<< HEAD
 
print("인사말 : {0}?  {1}님, 반갑습니다.".format(hi, boy))

# (new String("인사말 : {0}! {1}님. 반갑습니다.").format(hi, boy))

=======
print("인사말 : {0}! {1}님. 반갑습니다.".format(hi, boy))

# 자바 스타일
# (new String("인사말 : {0}! {1}님. 반갑습니다.")).format(hi, boy)

#%%

# 중괄호를 포맷으로 인식하지 않고 문자 자체로 처리
print("인사말 : {{{0}}}! {1}님. 반갑습니다.".format(hi, boy))

# ValueError: Single '}' encountered in format string
# print("인사말 : \{{0}\}! {1}님. 반갑습니다.".format(hi, boy))
>>>>>>> origin/master
