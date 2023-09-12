# def hello():
#     print("hello world!!!")
#
# hello()

# def add(a,b):
#     print(f"a:{a} b:{b}")
#     return a+b#True # False
#
# value = add(2,3)
# print(value)
# print(add(40,5))

def add(a=90, b=100):
    return f"addition of {a} and {b} is {a + b}"

print(add()) # default
print(add(a=10, b=20))
print(add(20,30))
print(add(b=20))
print(add(20))
print(add(10, a=20)) # error

