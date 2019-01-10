import xlrd  
####################################
adress = ("Book1.xlsx")# masir file excel 

wb = xlrd.open_workbook(adress)# baray tabdil kardan file excel be type:xlrdbook
sheet = wb.sheet_by_index(0) # baray tabdil kardan file excel be type:xlrdsheet

dynamic = [] # sakhte ye array ke meghdar haro brizim tosh

for i in range(sheet.ncols): # baraye ejraye halghe be andaze sutun
    print(sheet.cell_value(0, i)) # print kardan meghdar har sutun
    arv = sheet.cell_value(0, i) # rikhtan meghdar har sutun toye in moteghayer
    dynamic.append(arv) # ezafe kardan meghdar har sutun be arayeye dynamic
print(dynamic)# namayesh arrayeye dynamic ke meghdar har sutun ra darad