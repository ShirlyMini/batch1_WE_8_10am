# function or method - to do some task
# def func_name(parameter):
#    satement
#    return status

# call function
# function_name(parameter)
# simple function ----without retuen statement, and parameter

# def hello():
#     print("hello python")
#
# hello()

# function ----with return statement, without parameter
# def sumofvar():
#     a=10
#     b=20
#     return(a+b)
#
# print(sumofvar())

# function ----with return statement, with parameter

# def sumofvar(a,b):
#     print(f"sum of {a} and {b}")
#     return(a+b)
#
# var =sumofvar(20, 40)
# print(var)

# function ----with return statement, with positional parameter/arguments
# def sumofvar(a,  b, c=10,  d=20):
#     print(f"a:{a}")
#     print(f"b:{b}")
#     print(f"c:{c}")
#     print(f"d:{d}")
#     return(map(int,(a+b+c+d)))
# print(sumofvar(10,20,30,40))
#print(sumofvar(10,20,d=30))
# x=int(input("enter the input for x"))
# print(type(x))
# y=int(input("enter the input for y"))
# z=int(input("enter the input for z"))
# v=int(input("enter the input for v"))
# #print(sumofvar(x,y,d=v))
# print(sumofvar(x,y,d=v,c=y))

# function parameter as len of list ---- variable length as parameter
# non default parameters
# def sumofvar(n, *b):
#     print(b)
#     sum = 0
#     for i in range(n):
#         sum=sum+b[i]
#         print(sum)
#
# sumofvar(3,1,2,3)


# def sumofvar(a, b, c, *var):
#     #print(f"a: {a} \nb:{b}\nc: {c}")
#     #print(var[0]+ var[1]+ var[2])
#     print(f"a:{a}")
#     print(f"b:{b}")
#     print(f"c:{c}")
#     print(var)
#     for i in range(len(var)):
#         print(var[i])
# #
# sumofvar(20, 40, 60, 23, 44, 55)  #---- nondefualt parameter ---return tuple

# **var returns Dictionary
# defaulf parameters
# def dict_var_len(**var):
#     print(var)
#     for key, value in var.items():
#         if value < 10:
#             continue
#         print(f"{key}: {value}")
# #
# dict_var_len(a=10, b=3,c = 4, d=20, e=50)  #---- defualt parameter ---return dict

# def dict_var_len(var1, var2, c1,  **var):
#     print(var)
#     print(var1)
#     print(var2)
#     print(c1)
#
# dict_var_len("nondefault", "nondefault", "nondefault", a=10, b=3,c = 4, d=20, e=50)

# l1= (1,2,["a", "b", "c"], 3)
# l1[2][1]="d"
# print(l1)

