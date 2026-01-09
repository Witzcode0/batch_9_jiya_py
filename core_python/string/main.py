# In Python, a string is an immutable sequence of Unicode characters used to represent text.
#  Strings are one of the most fundamental data types in the language and are essential for handling text-based data, such as names, messages, and file contents. 

# Creating Strings

# string_name = 'value'
# string_name = "value"
# string_name = '''value'''
# string_name = """value"""
# string_name = str()
# print(type(string_name))

code = "python"

# p 0 -6
# y 1 -5
# t 2 -4
# h 3 -3
# o 4 -2
# n 5 -1

# indexing
# print(code[1])
# print(code[-3])

# slicing
# oht
# print(code[-2:-5:-1])
# print(code[-2:-5:1])

name = "nayan"

# print(name == name[::-1])

# concat
# first_name = "Brijesh"
# space = " "
# last_name = "Gondaliya"

# print(first_name+space+last_name)

# *
# **
# ***
# ****
# *****

# num = 5
# for row in range(1, num+1):
#     print(" "*(num-row), row*" *")


# str_name = str()
# print(dir(str_name))

# company = "bHaRAt fUtuRIst aI"
# print(type(company))
# print(len(company))

# print(company.lower())
# print(company.upper())
# print(company.title())
# print(company.capitalize())
# print(company.swapcase())
# print(company)

# center = "*"
# print(center.center(2))
# print(center.center(3))
# print(center.center(5,"-"))

# password = "admin13"

# print(password.isalpha())
# print(password.isdigit())
# print(password.isalnum())


# password = input("Password: ")
# upper_ = False
# lower_ = False
# digit_ = False
# spec_char = False
# at_least_8 = False

# if len(password) >= 8:
#     at_least_8 = True
#     for ch in password:
#         if ch.upper():
#             upper_ = True
#             continue
#         if ch.islower():
#             lower_ = True
#             continue
#         if ch.isdigit():
#             digit_ = True
#             continue
#         if not ch.isalnum():
#             spec_char = True
#             continue
#         print(ch)
# else:
#     print("Password is must be at least 8 char.")
# print(upper_, lower_, digit_, spec_char, at_least_8)
# if upper_ and lower_ and digit_ and spec_char and at_least_8:
#     print("Password is correct")
# else:
#     print("Incorrect password")

code = "pythonth"

# print(code.find("th", -5))

# string formating

name = "python"
price = 345.78
page = 400

# print("my book name is python and it's price is 345.78 and total page is 400.")
# sen = "my book name is ",name, " and it's price is ", price, " and total page is ", page, "."
# print(sen)
# print("my book name is ",name, " and it's price is ", price, " and total page is ", page, ".")
# print(f"my book name is {name} and it's price is {price} and total page is {page}.")
# print("my book name is {} and it's price is {} and total page is {}.".format(name, price, page))
# print("my book name is {1} and it's price is {0} and total page is {2}.".format(name, price, page))
# print("my book name is {1} and it's price is {2} and total page is {3}.".format(name, price, page))
# print("my book name is {1} and it's price is {2} and total page is {3}.".format(name, name, price, page))
# print("my book name is %s and it's price is %.2f and total page is %d." % (name, price, page))

    # Escap seq.
    # qoute matter

# print("brijesh gondaliya")
# print("brijesh go\ndaliya")
# print(r"brijesh go\ndaliya")

# print("brijesh go\\ndaliya")
# print("\\\\")
# print("\'")
# print("\tbrijesh")

# print("my name is \"brijesh gondaliya\"")
# print("my name is \'brijesh gondaliya\'")
# print("my name is 'brijesh gondaliya'")
# print('my name is "brijesh gondaliya"')

# email = "brijesh@gmail.com"

# print(email.endswith("@gmail.com"))
# print(email.startswith("brijesh"))

# nums = [1123, 4567, 8765, 3456]
# print("-".join([str(num) for num in nums]))

data = "     this is    something...     "

# print(data.replace("  ", " ").replace("  ", " ").strip())

# print(data.strip())
# print(data.lstrip())
# print(data.rstrip())


