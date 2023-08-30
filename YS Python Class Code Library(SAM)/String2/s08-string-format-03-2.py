# 문자열 포매팅(String Formatting)
# format 함수를 사용한 포매팅
# 포맷문자열.format(값, ...)
# 포맷은 중괄호({순번})로 감싼다.
# 자료형은 알아서 변환을 시킨다.

# 문자열과 정수를 복합적으로 써서 문자열 포매팅에 적용할 때
msg = "오늘의 날짜는 ({0})이며, 온도는 ({1})도 입니다.".format('2021-06-26', 28)
print(type(msg), msg)

msgfmt = "오늘의 날짜는 ({0})이며, 온도는 ({1})도 입니다."
print(type(msgfmt), msgfmt.format('2021-06-26', 26))

# 이름으로 넣기 : 파라미터 이름(인자이름)
msgfmt = "오늘의 날짜는 ({today})이며, 온도는 ({temp})도 입니다."
print("이름으로:", msgfmt.format(today='2021-12-28', temp=-1))

# 이름으로 넣기
msgfmt = "오늘의 날짜는 ({today})이며, 온도는 ({temp})도 입니다."
now='2021-12-28'
tp=-10
print("이름 순서 바꿈:", msgfmt.format(temp=tp, today=now))

