# poly - many, morphism - forms

# - method over-loading - compile time/ static binding - not support in python
# - method overridding - runtime/ dynamic binding - support

# class Math1:
#     def sum(self, num1, num2):
#         return num1 + num2
    
#     def sum(self, num1, num2, num3):
#         return num1 + num2 + num3
    
# obj = Math1()
# print(obj.sum(10, 20)) # TypeError: Math1.sum() missing 1 required positional argument: 'num3'
# print(obj.sum(10, 20, 30))


# class Math1:
#     def sum(self, *args):
#         return sum(args)
# obj = Math1()
# print(obj.sum(10,20, 30))

# class Math1:
#     def sum(self, num1, num2):
#         print("Parent class")
#         return num1 + num2
    
# class Math2(Math1):
#     def sum(self, num1, num2):
#         print("Child class")
#         return num1 + num2
    
# obj = Math2().sum(10,20)

