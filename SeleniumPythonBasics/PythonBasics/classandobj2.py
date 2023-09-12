# # instance variable
# # class - bounded to the class, declared insdie the class, access outside using object
# # instance - bounded to the object, instance var sould be declared inside __init__
# # __init__- constuctor
# # constructor will initiate the variable at the time of memory allocation
#
# class instancevar:
#     # class variable
#     num =100
#     # counstuctor will initaite the variable declaration
#     def __init__(self,a ,b):
#         self.a = a
#         self.b = b
#         print(f"printing {self.a} and {self.b}")
#
#         def add(self):
#             print(f"addition of {self.a}, {self.b} and {self.num}")
#             print(f"addition of {self.a}, {self.b} and {instancevar.num}")
#         add(self)
#
#
#
# # instantiation, object creation __init__ function will call by default
# # initiate all the var, fun inside the __init__ function
# obj = instancevar(10, 20)
# #obj.num=2000
# #obj.add()
#
# obj2 = instancevar(100, 200)
# #obj2.add()
# # constructor and destuctor
# class constructoranddesstructor:
#
#     def __init__(self):
#
#         print("inside constructor")
#     # explicitly call the destructor in python
#     def __del__(self):
#         print("inside destructor")
#
# obj=constructoranddesstructor()
# print(obj)
#
# obj2=constructoranddesstructor()
# print(obj2)
# del(obj)
# del(obj2)
# print(obj)
# print(obj2)



