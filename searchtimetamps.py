import os,sys

path='C:\\Users\\PUJITHA\\AppData\\Local\\Programs\\Python\\Python36\\Timestamps'
dirs=os.listdir(path)
print("list of all the contetnts in the TimeStamps Library ")
print(dirs)
# Converting the directory names to integers
dirs=list(map(int,dirs))
dirs.sort()
print("sorted list of dirs are",dirs)


# finding the list of timestamps greater than particular value 
def searchtimestampmax(filteredlist,timestamp_maxnumber):
	filteredlist = list(filter(lambda x: x > timestamp_maxnumber, dirs))
	print(filteredlist)

# finding the list of timestamps lessthan particular value
def searchtimestampmin(count,timestamp_minnumber):
	filteredlist = list(filter(lambda x: x < timestamp_minnumber, dirs))
	print(filteredlist)

# finding the list of timestamps greater than particular value and limit on elements
def searchtimestampmax(count,timestamp_maxnumber):
     filteredlist = list(filter(lambda x: x > timestamp_maxnumber, dirs))
     positon=[i for i, j in enumerate(filteredlist) if j == timestamp_maxnumber]
     print(filteredlist[0:count])

# finding the list of timestamps less than particular value and limit on elements
def searchtimestampmin(count,timestamp_maxnumber):
     filteredlist = list(filter(lambda x: x < timestamp_minnumber, dirs))
     positon=[i for i, j in enumerate(filteredlist) if j == timestamp_maxnumber]
     s=count
     print(filteredlist[0:-s])
     
     
                              
	
