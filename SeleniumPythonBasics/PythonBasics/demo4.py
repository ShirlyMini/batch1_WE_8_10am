#~ = not
# ~x = -x-1
# 3 = 0011
# ~ 3 = 1100 -4

# print(~12)

# map() - maps a function with a itertor
# syntax = map(fucn, iter like list, tuple etc)
# a=(1,2,"3", 4,"5")
# print(a)
# print(tuple(map(int, a))) # convert string int to int in a list
#
# def sqr(num):
#     return num*num
#
#
# a=(1,2,3, 4, 5)
# # print(list(map(sqr, a)))
# for i in a:
#     print(sqr(i))

# lambda functions defining a function in single line
# syntax = lamba arguments: ccondition

# lamb_fuc = lambda num: num*num
# print(lamb_fuc(3))

# lamb_fuc2 = lambda out1, out2: out1==True and out2 == True
# print(lamb_fuc2(True, True))
# print(lamb_fuc2(False, True))
# print(lamb_fuc2(True, False))

lamb_func3 = lambda a,b: a+b
print(lamb_func3(1,2))
print(lamb_func3("str1", "str2"))