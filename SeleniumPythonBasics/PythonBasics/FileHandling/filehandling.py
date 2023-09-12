# create and access files

# create file
# modes= w write [create or write on exisiting file]
# fh_obj = open("file1.txt", "w") # file not there creates a file or opens exisiting file
# fh_obj.write("this is the first line")
# fh_obj.close()

# mode - r [read the content of the file]
# fr_obj=open("file1.txt", "r")
#print(fr_obj.read()) # read whole content as str
#print(fr_obj.readline()) # return very first line
# print(fr_obj.readlines()) # return whole content as list
# fr_obj.close()

# mode - a -append if the file is not there it will create the file and add the data
#if file is exsisting it will add the line at the end of the content

# fh=open("file2.txt", "a") # file not execited with append mode
# fh.write("this line is appended")
# fh.close()

# fh=open("file1.txt", "a")
# fh.write("this line is appended")
# fh.close()

# with keyword
# with open("file1.txt", "r") as fh:
#     print(fh.readline())

list1=[1,2,3,4,5,6,7,8,9]

with open("file3.txt","w") as fh:
    for i in list1:
        fh.write(str(i)+"\n")

with open("file3.txt", "r") as fh:
    print(fh.readlines())