import numpy
import xlrd

def motion(addr):
    WorkBook = xlrd.open_workbook(addr)
    sheet = WorkBook.sheet_by_index(0)
    amotion = []
    angles = []
    for a in range(sheet.nrows):
        for b in range(sheet.ncols):
            meghdr = sheet.cell_value(a, b)
            angles.append(int(meghdr))
        amotion.append(angles)
        angles = []
    return amotion

print(motion("Book1.xlsx"))