import xlrd  # ketabkhune marbut 


adress = ("Book1.xlsx") # mahal fiel excel  

wb = xlrd.open_workbook(adress)# baray tabdil kardan file excel be type:xlrdbook
sheet = wb.sheet_by_index(0) # baray tabdil kardan file excel be type:xlrdsheet

sheet.cell_value(0, 0) # baraye daryafte meghdar satr0 , sutun0 

print(sheet.nrows) # baraye namayesh tedad satr
print(sheet.ncols) # baraye namayesh tedad sutun

for i in range(sheet.ncols): # ejraye halghe be tedad sutun
    print(sheet.cell_value(0, i))# namayesh meghdar har sutun

for i in range(sheet.nrows): # ejraye halghe be tedad satr
    print(sheet.cell_value(i, 0)) # namayesh meghdar har satr

