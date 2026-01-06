# types of functions
# - user define
# - built-in

# syntax :
# def function_name(paras):
#     block of code

# function call
# function_name(vals)

# def add(num1, num2):
#     print(num1 + num2)

# add(10, 20)
# add(100, 200)

# types of parameters
# 1. positional para
# 2. default/ keyword para
# 3. variable len para

# def add(a, b, c):
#     print(a+b+c)

# add(10, 20) # TypeError: add() missing 1 required positional argument: 'c'
# add(10, 20, 30)

# def bill(tomato, potato, discount=5):
#     total = tomato + potato
#     discount_amount = (total * discount)/100
#     print(total-discount_amount)

# bill(500, 100, discount=10)

# # 100 - 100%
# 100% - 100
# 5% - ?
# (5 * 100)/100  = 5

# *args - tuple
# **kwargs - dict

# def add(*nums):
#     # print(sum(nums))
#     total = 0
#     for num in nums:
#         total += num
#     print(total)

# add(10,20, 30, 40, 50, 60,70,80,90,100)

# def bill(discount=5, **items):
#     # print(items, discount)
#     start = 0
#     for key, value in items.items():
#         start+=1
#         print(f"item-{start}: {key}, price : {value}")

# bill(10, tomato=10, potato=20, onion=30)


# sum = lambda num1, num2 : num1 + num2

# print(sum(10, 20))

nums = [1,2,3,4,5,6,7,8,9,10]
# 1+2
# 2+2
# 3+2

# def add_2(num):
#     return num + 2
# print(list(map(lambda num:num+2, nums)))

# print(list(filter(lambda num:num % 2 == 0, nums)))
# print(list(filter(lambda num:num % 2 != 0, nums)))

# g_var = 10

# def test():
#     g_var = 20
#     print(g_var)

# test()
# print(g_var)


# g_var = 10

# def test():
#     global g_var
#     g_var = 20
#     print(g_var)

# test()
# print(g_var)


# def outer():
#     print("Outer function")
#     def inner():
#         print("Inner function")
#     return inner()

# outer()

# def inner(callback):
#     print("Inner")
#     callback()


# def outer():
#     print("Outer")

# inner(outer)

# def upper_case(func):
#     def wrapper():
#         res = func().upper()
#         print(res)
#         return res
#     return wrapper

# def title_case(func):
#     def wrapper():
#         res = func().title()
#         print(res)
#         return res
#     return wrapper

# @upper_case
# @title_case
# def test():
#     return input("Enter something... ")
# print(test())

# def num_generator():
#     yield 1
#     yield 2
#     yield 3

# nums = num_generator()
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# def num_gen():
#     end = int(input("Enter a num : "))
#     for num in range(1, end+1):
#         yield num

# print(list(map(lambda num:num**2, num_gen())))

# def add(a, b):
#     return a + b


# def multi_returns():
#     return 1,2,3,4,5,6

# print(multi_returns())