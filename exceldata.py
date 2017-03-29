import xlsx
book = xlsx.open_workbook("vendor.xls") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
 
sheet = book.sheet_by_name("sheet1") #we can pull by name 
r = sheet.row(0) #returns all the CELLS of row 0,
c = sheet.col_values(0) #returns all the VALUES of row 0,
 
data = [] #make a data store
for i in xrange(sheet.nrows):
  data.append(sheet.row_values(i))
