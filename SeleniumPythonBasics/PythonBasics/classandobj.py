# object oriented programming language
# class, object, inheritance, polymorphysm, data abstraction, encapsulation

# class - blue print, template which all the data
#
# class empty:
#     pass # do-northing statement
#
# # obj - binding your data store it in single mem location
# # instance - an obj, build your data, access data in class
# obj=empty()
# print(obj)
# obj1=empty()
# print(obj1)
# obj2=empty()
# print(obj2)
# class with class variable---static data
class classdata:
    num1=100
    num2=200
    # self should be passed as parameter in ever func defined inside class
    # instance of the class binds all the class data, without self we cannot access the data
    def add(self, a,b):
        # inside the class accessing the class variables num1 and num2 using class name
        print(f"addintion of {classdata.num1} {classdata.num2} is {classdata.num1+classdata.num2}")
        print(f"addintion of {a} {b} is {a+b}")

    def sub(self, a,b):
        # inside the class accessing the class variables num1 and num2 using class name
        # class variables can also be accessed using self parameter
        print(f"Subraction of {self.num1} {self.num2} is {self.num1-self.num2}")
        print(f"Subraction of {a} {b} is {a-b}")

#obj=classdata()   # store it in single location
# outside the class ...class variables can be accessed using obj
# print(obj.num1)
# print(obj.num2)
#obj.add()#----backend obj.add(obj/classname)
# obj.add(10,20)#----backend obj.add(obj/, 10, 20)
# obj.sub(50,20)
# obj2=classdata()
# obj2.num1=300
# print(obj2.num1)
# print(obj2.num2)
# obj2.add(40,200)#----backend obj.add(obj, 10, 20)

print(dir(classdata))

