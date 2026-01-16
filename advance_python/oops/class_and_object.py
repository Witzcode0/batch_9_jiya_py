# syntax :
# class ClassName:
#     block of code

# class ClassName:
    # data memeber [attributes or properties]
    # member function [method or behavior]

# class Person:
#     pass

# Syntax of object
# obj_name = ClassName()

# height1 = 10
# width1 = 10

# def triarea(h, w):
#     return 0.5 * h * w

# print(height)
# print(width)
# print(triarea(height1, width1))

# height2 = 100
# width2 = 100
# print(triarea(height2, width2))

# class Triangle:
#     # data memeber [attributes or properties]

#     # member function [method or behavior]
#     # def triarea(yoyo, h, w):
#     #     print(type(0.5), type(h), type(w))
#     #     return 0.5 * h * w

#     def triarea(self, h, w):
#         print(type(0.5), type(h), type(w))
#         return 0.5 * h * w
    
# t1 = Triangle()
# t2 = Triangle()
# print(t1.triarea(10, 20))
# print(t2.triarea(100, 200))


# class Triangle:
#     # data memeber [attributes or properties]
#     def __init__(self, height, width):
#         print("I will auto call when object is created of this class")
#         self.h = height
#         self.w = width
#     # member function [method or behavior]
#     def triarea(self):
#         print(type(0.5), type(self.h), type(self.w))
#         return 0.5 *self.h * self.w
    
# t1 = Triangle(10, 20)
# t2 = Triangle(100, 200)
# print(t1.triarea())
# print(t2.triarea())

class Auth:
    class Register:

        def R(self):
            print("This is a register method")

    class Login:
        def L(self):
            print("This is a login method")
        
inner_obj_reg = Auth().Register().R()

inner_obj_l = Auth().Login()
inner_obj_l.L()
