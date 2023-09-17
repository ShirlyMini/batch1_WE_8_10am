# string
# convert string to list
# list to string
# strip()

# str1="selenium is a testing framework"
#
# # split the sentence to list based on spaces
#
# splited_str = str1.split() # default space
# print(splited_str)
#
# list_len=len(splited_str)
# for i in range(list_len):
#     if splited_str[i] == "selenium":
#         splited_str[i] = "pytest"
#
# print(splited_str)
# # convert list to string
# new_str1="**".join(splited_str)
# print(new_str1)

# #####strip will remove the delimiter based on input

str1="000hp gas limited000"
print(str1.strip("0"))
print(str1.lstrip("0"))
print(str1.rstrip("0"))

str1="   hp gas limited   "
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())

