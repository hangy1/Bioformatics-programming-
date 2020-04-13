import os
#current working directory
print(os.getcwd())

#change directory(cd)
os.chdir(path='/Users/hangyin/BINF6200/Bioformatics-programming-')

#remove:
#os.remove("path/file")

#rename
#os.rename(source_file_name, destination_file_name)

#join file or path
file_name = os.path.join(os.getcwd(),"join.txt")
print(file_name)

#split path and extension
a = os.path.split(file_name)
print(a)
print(a[1].split(".")[-1])
print(os.path.splitext(file_name))

#list of files
#with os.scandir(os.getcwd()) as entries:
    #for entry in entries:
        #print(entry.name/path/stat)



