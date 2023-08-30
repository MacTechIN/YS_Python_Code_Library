# escape character
# 백슬래시(\) 기호를 사용

# 개행문자: Line Feed
# 키보드에서 Enter 키를 치면 내부에 입력되는 코드(\n)
print("one\ntwo\nhree")

print('-' * 30)
print("one", end='\n')
print("two", end='\n')
print("three", end='\n')

print('-' * 30)
# 탭(Tab) : \t
print('123456789012345678901234567890')
print("one", end='\t')
print("two", end='\t')
print("three")

print('12345678901234567890123456789012345678901234567890')
print("one\ttwo\tthree\t1234567890123\tABC")
