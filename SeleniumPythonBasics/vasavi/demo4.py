# file handling

# read/ wriet any conetent in file

# file not exit
# fh = open("file.txt", "w")
# fh.write("this is my first line") # file already exsist overwriet
# fh.close()

# fh = open("file.txt", "r")
# print(fh.read())
# fh.close()

fh = open("file11.txt", "a")
fh.write("\nthis is my second line-overwritten")# file already exsist append at the end
fh = open("file11.txt", "r")
print(fh.read())
fh.close()