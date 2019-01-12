import numpy
from time import sleep
import pypot.dynamixel as dynamixel
import xlrd

excel_file = "/media/root/Game/Professional/Project/Python/Book1.xlsx"

port = dynamixel.get_available_ports()[0]
dxl = dynamixel.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))

WorkBook = xlrd.open_workbook(excel_file)
sheet = WorkBook.sheet_by_index(0)

def get_pos_x(line):
    dynamic = []
    for i in range(sheet.ncols):
        arv = sheet.cell_value(line, i)
        dynamic.append(int(arv))
    return dynamic 

def set_pos(poses):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=(poses[i]-512)*0.29
    dxl.set_goal_position(dicts)

def get_pos():
    return dxl.get_present_position(tuple(fids)) #Tuple

dxl.enable_torque(fids)


dxl.disable_torque(fids)
