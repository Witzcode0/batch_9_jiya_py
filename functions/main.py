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
