# you have base/parent/super class and child/derived class
# base inheritance - one parent,  one child
class parent:
    def __init__(self, a, b):
        self.a= a
        self.b = b
        print(f"executing parent constructor \n VRAIABLES are {self.a} {self.b}")

    def parentmethod(self):
        print(f"parentmethod adding two number {self.a} and {self.b} is {self.a+self.b}")
        print("i am inside the parent method")

class child(parent):
    # def __init__(self, a, b):
    #     #self.a = a
    #     #self.b = b
    #     parent.__init__(self, a, b) # to be clarified in next session

    def childmethod(self):
        print(f"childmethod adding two number {self.a} and {self.b} is {self.a + self.b}")
        print("i am inside the child method")
        # access parent method thru child method
        self.parentmethod()

obj = child(2,5)
obj.childmethod()
# to call the parent method
# obj.parentmethod()