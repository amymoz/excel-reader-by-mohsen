import numpy
from time import sleep
import pypot.dynamixel as dyn
import xlrd

excel_file = "Book1.xlsx"

port = dyn.get_available_ports()[0]
dxl = dyn.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))

WorkBook = xlrd.open_workbook(excel_file)
sheet = WorkBook.sheet_by_index(0)

def motor_poses(line):
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

set_pos(motor_poses(0))
sleep(3)

dxl.disable_torque(fids)
