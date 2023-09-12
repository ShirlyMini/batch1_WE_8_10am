# python package -library
# built in lib - math, sys
# user defined lib - python package - allows the use to create a method and class in file and access seperately in folder
# POM -page object model - login page(file) - logout page (file) - how to access the function or class from a file?
# package means folder


# how to import libraries
# built-in lib
# import math
# print(dir(math)) # provide all attribultes the mat lib
# print(math.pi * math.pow(3,2))

# user defined pkg/lib
# we can use the package with __init.py to initalize the attributes at the time of import
# Otherwise you can use without __init__.py still python will identify it as package(condition applies >3.3 version)

from folder1 import sample

sample.sample()


import folder
from folder import sample

sample.sample()