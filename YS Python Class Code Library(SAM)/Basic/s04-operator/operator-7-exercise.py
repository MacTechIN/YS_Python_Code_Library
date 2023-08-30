# [문제3]
# 한 달 기본급이 400만원이다.
# 분기별로 보너스가 월 급여의 30%가 지급된다.
# 세금은 월 기본급의 3%이다.
# 보너스에 대한 세금은 없다.
# 월 세후 수령액은 얼마인가?
# 연 수령액(세후 총 수령액)은 얼마인가?
# 총 세금은 얼마인가?

#%%
# 한 달 급여
salary = 4000000
print("급여: ", salary)

# 분기별 보너스
bonus = salary * 0.3
print("분기별 보너스: ", bonus)

# 세금
tax = salary * 0.03
print("세금: ", tax)

# 월 수령액
month_salary = salary - tax
print('월수령액', month_salary)

# 총 연봉
total = salary * 12
total += bonus * 4
print("총연봉: ", total)

# 연 수령액
year_salary = month_salary * 12
year_salary += bonus * 4
print("연수령액: ", year_salary)

# 총세금
tot_tax = tax * 12
print("총 세금: ", tot_tax)


