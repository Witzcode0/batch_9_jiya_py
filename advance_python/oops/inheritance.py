# parent/base class 
# child/derived class

# types of inheritance
# 1. single
# A -> B

# class A:
#     def a(self):
#         print("I am from class A")
# class B(A):
#     def b(self):
#         print("I am from class B")

# obj = B()
# obj.a()
# obj.b()
    

# 2. multilevel 
# A -> B -> C -> D

# class A:
#     def a(self):
#         print("I am from class A")
# class B(A):
#     def b(self):
#         print("I am from class B")
# class C(B):
#     def c(self):
#         print("I am from class C")
# class D(C):
#     def d(self):
#         print("I am from class D")

# obj = D()
# obj.a()
# obj.b()
# obj.c()
# obj.d()
    

# 3. multiple
# A, B -> C

# class A:
#     def a(self):
#         print("I am from class A")
# class B:
#     def b(self):
#         print("I am from class B")
# class C(A, B):
#     def c(self):
#         print("I am from class C")

# obj = C()
# obj.a()
# obj.b()
# obj.c()

# 4. herarchicle
# A -> B, C  B -> B1, B2
#            C -> C1, C2

class A:
    def a(self):
        print("I am from class A")

class B(A):
    def b(self):
        print("I am from class B")

class B1(B):
    def b1(self):
        print("I am from class B1")
class B2(B):
    def b2(self):
        print("I am from class B2")

class C(A):
    def c(self):
        print("I am from class C")

class C1(C):
    def c1(self):
        print("I am from class C1")
class C2(C):
    def c2(self):
        print("I am from class C2")


obj = C2()
# obj.a()
# obj.c()
# obj.c2()
# print(C2.__mro__)
# print(C2.mro())

# 5. hybrid
# A -> B,C    B, C -> B1, B2

