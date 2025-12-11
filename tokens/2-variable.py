# a variable is a named storage location used to hold data. It acts as a label or a container for a value, allowing you to store, reference, and manipulate that data throughout your program.

# syntax
# data_type variable_name = value; # C, C++
# variable_name = value

num = 10

# print(num)
# print(type(num)) # <class 'int'>

# num1 = 10
# num2 = 10
# num1 = num2 = 10
# print(num1, num2)

# num1, num2 = 10, 10
# print(num1, num2)

# num = input("Enter your number: ")
# print(num)
# print(type(num)) # <class 'str'>

# num1, num2 = input("Enter a num1 and num2 sep. by comma: ") # ValueError: too many values to unpack (expected 2)
# print(num1, num2)

# num1, num2 = input("Enter a num1 and num2 sep. by comma: ").split(",")
# print(num1, num2)

# num1, num2, num3 = input("Enter a num1, num2 and num3 sep. by comma: ").split(",")
# print(num1, num2, num3)
# print("10, 20, 30".split(",")) # ['10', ' 20', ' 30']

# num1, num2, num3 =  ['10', ' 20', ' 30']
# print(num1, num2, num3)

# boy_name = "Brijesh"
# girl_name = "Jiya"

# print(id(boy_name))
# print(id(girl_name))

# num1 = 10
# num2 = 10
# print(id(num1))
# print(id(num2))

# l1 = [10]
# l2 = [10]

# print(id(l1) == id(l2)) # False

