# 문자열 인덱싱
# 문자열의 위치를 참조
# 시작위치 : 0부터 시작
# 참조방법 : 문자열[인덱스]
# 참조범위 : 0부터 문자열의 길이에서 -1까지
# 제약사항 : 인덱싱을 통한 참조를 통해서 개별적인 문자를 바꿀 수는 없다.

# 한글
sx = "안녕하세요?"
print('len(sx):', len(sx))  # 문자열의 길이
print(sx[0])  # 안
print(sx[1])  # 녕
print(sx[2])  # 하
# print(sx[25]) # IndexError: sxing index out of range

lastpos = len(sx) - 1
lastsx = sx[lastpos]
print("lastpos=", lastpos, "lastsx=", lastsx)

print("마지막문자: ", sx[len(sx) - 1]) # 마지막 문자 : ?

