'''
import xlrd  
loc = ("Book1.xlsx") 
wb = xlrd.open_workbook(loca) 
sheet = wb.sheet_by_index(0) 
# For row 0 and column 0 
sheet.cell_value(0, 0) 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
  
#shomare row va shomare column
print(sheet.nrows)
print(sheet.ncols)
for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i))
for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0)) 
print(sheet.row_values(1)) 
'''
import xlrd  
loc = ("Book1.xlsx") 

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

dynamic = []
for i in range(sheet.ncols):
    arv = sheet.cell_value(0, i)
    dynamic.append(arv)
    print(sheet.cell_value(0, i))
print(dynamic)