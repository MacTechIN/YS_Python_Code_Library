# 인스턴스

# type : 자료형을 알려 준다.
f = 0.1234
print('type:', type(f)) # float(실수형)

fs = str(type(f))
print('type:', fs)

#%%
# isinstance()
print('instance: float?', isinstance(f, float))
print('instance: int?', isinstance(f, int))
print('instance: str?', isinstance(f, str))
print('instance: bool?', isinstance(f, bool))


#%%

ft = type(f) # float
print(isinstance(f, ft))
print(isinstance(f, type(f)))

print('instance: str?', isinstance(f, str))
print('instance: float?', isinstance(f, float))
