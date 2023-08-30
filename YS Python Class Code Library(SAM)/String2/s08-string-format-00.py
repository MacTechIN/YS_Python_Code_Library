num = 30
numformat = "현재 온도는 {0}도 입니다.".format(num)
print(numformat)

#%%
num = 30
numformat = "현재 온도는 %d 도 입니다."
print("현재 온도는 %d 도 입니다." % 3)
print(numformat % 3)

#%%

print(numformat.format(args, kwargs))