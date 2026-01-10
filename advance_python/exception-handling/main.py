# try, except, else, finally, assert. raise
# file:///C:/Users/admin/AppData/Local/Programs/Python/Python313/Doc/html/library/exceptions.html#RuntimeError
# print("start")
# try:
#     a = 10
#     b = int(input("Enter numbe: "))
#     res = a/b
# except ValueError:
#     print("ERROR : invalid literal for int() with base 10: 'jhgsdkfuyhsgdukf'")
# except ZeroDivisionError:
#     print("You can not divide by zero.")
# except Exception as err:
#     print(err)
# else:
#     print(res)
# finally:
#     print("I will always print")
# print("end")

# bal = 1000
# wb = 1500
# assert bal > wb, "Insufficent balanace"

# if wb > bal:
#     raise ValueError("Insufficent balance")
# else:
#     print("Now, your remainaing balance is : ", bal-wb)