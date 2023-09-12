# print(var) ---> NameError: name 'var' is not defined
# try:
#     #var=10
#     print(var)  #
# except Exception as e: #
#     print("some error happened in the try block")
#     print(e)# to print python complier msg


# try:
#     a=0
#     if a==0:
#         raise Exception("try block a is still 0") # inducing the error
#         #print("a is still zero")
#     else:
#         print("successfully exited try block")
#
# except Exception as e:
#     print("some error happened in the try block")
#     print(e)# to print python complier msg, if raise or assert it will print userdefined msg

# try:
#     with open("test1.txt", "w") as filehandle:
#         filehandle.write("writing something")
#         filehandle.close()
#     with open("test1.txt", "r") as reader:
#         print(reader.read())
#         reader.close()
# except Exception as e:
#     print(f"error msg:{e}")

try:
    reader = open("test1.txt", "r")
    print(reader.readlines())
except Exception as e:
    print(f"error msg:{e}")
finally: # executed always and eg. for cleanup process
    #reader = open("test2.txt", "r")
    reader.close() # cleanup
    print("finally block")