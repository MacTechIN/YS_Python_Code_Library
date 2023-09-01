from functools import partial 


# 덧셈, 곱샘을 수행하는 함수

def add_mul(choice, *args):
    if choice == "add":
        result = 0 
        for i in args:
            result = result + i
			
    elif choice == "mul":
        result =1 
        for i in args:
            result = result * i 
    return result 





#%%

#복잡한 인수구조를 가진 함수를 
ss = add_mul("add", 1,2,3,4,5)
dd = add_mul("mul", 1,2,3,4,5)

print(ss)
print(dd)


#%%
#간단한 함수를 만들수 있다. 

def add(*args):
	return add_mul('add', *args)


def mul(*args):
	return add_mul('mul', *args)


print("add : ", add(1,2,3,4,5,))

print("mul : ", mul(1,2,3,4,5))


#%%
#기존 함수를 이용해서 새로운 함수를 만들어준다, 

add = partial(add_mul, 'add')
mul = partial(add_mul, 'mul')

print(add(1,2,3,4,5))
print(mul(1,2,3,4,5))




# %%

add2 = partial(add_mul, "add",100)

print(add2(100)) 