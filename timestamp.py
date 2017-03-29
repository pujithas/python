import os,sys
from os import walk

path='C:\\Users\\PUJITHA\\AppData\\Local\\Programs\\Python\\Python36\\Timestamps'
dirs=os.listdir(path)
print("list of all the contetnts in the TimeStamps Library ")
print(dirs)

# Adding the directory contents in list data structure
f = []
for (filenames) in walk(path):
    f.extend(filenames)
    break

print(f)
