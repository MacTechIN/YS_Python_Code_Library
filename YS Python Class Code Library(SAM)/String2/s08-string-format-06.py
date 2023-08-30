# 문자열 포매팅(String Formatting)
# f"{변수}"

a = 10
b = 10000
c = 1000
d = 90

print("[포인트 현황]")
print(f"a의 포인트는 ({a})입니다.")
print(f"b의 포인트는 ({b})입니다.")
print(f"c의 포인트는 ({c})입니다.")
print(f"d의 포인트는 ({d})입니다.")
print(f"모든 포인트 목록:{a},{b},{c},{d}")

#%%
pointfmt = f"{a},{b},{c},{d}"
print("모든 포인트 목록:", pointfmt)

#%%

title = "쇼핑목록"
catalog = "상품목록"
htmlh1 = f"<h1>{title}</h1>"
htmlp = f"<p>{catalog}</p>"
print(htmlh1)
print(htmlp)
#%%

today = '2021-06-26'
temp = 28
msg = f"오늘의 날짜는 ({today})이며, 온도는 ({temp})도 입니다."
print(msg)

#%%
# 연산식을 넣을 수 있다.
# temp + 2
msg = f"내일의 온도는 ({temp + 2})도 입니다."
print(msg)
#%%

