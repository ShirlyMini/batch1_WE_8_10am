# string declaration
# to comment single line use  '#'
# to comment multiple line use ''' ''' or """ """
"""a ="it's me python"
b ='"python"'
print(a, b)

# revesed
l1 = [3,55,22,11]
print(sorted(l1, reverse=True))
print(l1[::-1])"""
#list pop, extend, remove

# # Dictionary - key, value pair - unordered
# # key unique , value can be duplicated
# dict1 = {1: "one", 2: "second"}
# print(dict1)
# print(dict1[1])
# # add new key:pair
# dict1[3]="third"
# print(dict1)
# # another method to add key:pait
# dict1.update({4:"four"})
# print(dict1)
# dict1.update({6:"six"})
# dict1.update({5:"fifth"})
# print(dict1)
# dict2 = {"3": 'third', "python": 'one', 2: 'second', "hello": 'four', 6: 'six', 5: 'fifth'}
# print(dict2)
# print(dict2["python"])
#
# # remove key: pair
# dict2.pop("python")
# print(dict2)
# #del dict2 ----> to delete entire dict
# del dict2[2] # ----> another method removes key: pair
# print(dict2)
# # to update exisiting one
# dict2["hello"] = "world"
# print(dict2)
#
# # clear dcit
# dict2.clear()
# print(dict2)

# to create empty list
# l1 =[]
# l2 = list()
# print(l1, l2)

# to create empty dict
# d1={}
# d2=dict()
# print(d1, d2)

# operator +, -, *,/, %
# int
# print(5+6)
# print(5-6) # ~ to be explained in next lecture
# print(45*6)
# print(65/6) # division without round off
# print(65//6) # floor division with round off
# print(95%6)

# string, list --------(+, * will not work for dict)
# print("python"+ "world") # will work only on strings
# print("python"* 5) # repeat
# l1=[1,2,3]
# print(l1+l1) # combine list
# print(l1*4) # combine and repeat the list


##############################################################################
# IF conditions
###########################################################################
# >, >=, <, <=, ==, != used for conditions
# print(4>3)
# print(4<3)
# print(4>=4)
# print(4<=4)
# print(4==4)
# print(4!=4)

# or, and, not used for conditions
# syntax:
#if (condition):
#   something
# else:
#   something
# indentation - 4 space or 1 tab
# odd or even
# n = 7
# if n%2 == 0:
#     print("even")
# else:
#     print("odd")
# defining
# print("even" if n%2==0 else None) # else should be mention, should have single statment in a if block

# None, "", '' is null charcter
# if ...elif... else
# print odd or even only greater than 10
# n = 18
# if n%2 == 0 and n>10:
#      print("even")
# elif n%2 != 0 and n>10:
#     print("odd")
# else:
#      print("error number is less than 10")

# nested if else

# n = 7
# if n>10:
#     if n%2==0:
#         print("even")
#     else:
#         print("odd")
#     print("number is greater than 10")
# else:
#      print("error number is less than 10")

################################################################3
# For loop
##########################################################
#range
# n=6
# for value in range(2,n+1):
#     print(value)

#string
# string="python"
# for value in string:
#     print(value)

#list
# list1=["python", "world", "hello"]
# print(len(list1))
# for value in range(len(list1)):
#      print(list1[value])

# if else in for loop
# list1=["python", "java", "world", "hello", "script"]
#
# for value in list1:
#      if value=="world":
#          print(value)
#          print("inside if statemet")
#          break
#      else:
#          print(value)
#          print("inside else statement")
# print("outside FOR LOOP")

# Continue---skip the remaining statements inside the loop

# list1=["python", "java", "world", "hello", "script"]
#
# for value in list1:
#       if value=="world":
#           continue
#       print(value)

# for value in list1:
#       if value=="world":
#           continue
#       print(value)
#       print("inside else statement")
# print("outside FOR LOOP")




