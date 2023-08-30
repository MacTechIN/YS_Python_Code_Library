# input() 명령어
# 키보드로부터 내용을 입력
# 변수 = input('안내문자')
# input() 함수가 리턴하는 자료형은 문자열

abc = input('값을 입력하세요: ')

print(abc)
print(type(abc))    # str : 문자열, string의 약자

num = int(abc)      # 문자열 -> 숫자
print(num, type(num)) # int

#%%

# 문자열과 숫자 연산(+, -) 오류
# TypeError: can only concatenate str (not "int") to str
# two = abc + num

#%%

print('-' * 50)

three = abc * num
print(three)
