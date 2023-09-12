
# you have base/parent/super class and child/derived class
# multiple inheritance - one or more parent,  one child
class parent1:
    # def __init__(self, a, b):
    #     self.c = a
    #     self.d = b
    #     print(f"executing parent1 constructor \n VRAIABLES are {self.c} {self.d}")

    def parent1method(self):
        print(f"parent1method adding two number {self.a} and {self.b} is {self.a+self.b}")
        print("i am inside the parent1 method")

class parent2:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        #parent1.__init__(self, 3, 4)# to call the parent1  explicitly
        print(f"executing parent2 constructor \n VRAIABLES are {self.a} {self.b}")

    def parent2method(self):
        print(f"parent2method adding two number {self.a} and {self.b} is {self.a + self.b}")
        print("i am inside the parent2 method")
# method resolution order
# python interpreter will sreach variables in child , parent class order
# interpreter will construct first parent constr if ch
class child(parent1, parent2):
    def __init__(self):
         #self.a = a
         #self.b = b
         parent1.__init__(self, 44, 55) # if parent1 and parent2 const to be called --call explicitly
         parent2.__init__(self, 20, 30) #

    def childmethod(self):
        print(f"childmethod adding two number {self.a} and {self.b} is {self.a + self.b}")
        #print(f"childmethod adding two number {self.c} and {self.d} is {self.c + self.d}")
        print("i am inside the child method")
        # access parent method thru child method
        # self.parentmethod()

obj = child(22,33)


obj.childmethod()
obj.parent1method()
obj.parent2method()