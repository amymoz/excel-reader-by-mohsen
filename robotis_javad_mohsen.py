import numpy
from time import sleep
import pypot.dynamixel as dyn
from excelreader import motion 

port = dyn.get_available_ports()[0]
dxl = dyn.DxlIO(port)
fids = dxl.scan(ids=list(range(19)))

def set_pos(poses):
    dicts={}
    for i in range(0,len(fids)):
        dicts[fids[i]]=(poses[i]-512)*0.29
    dxl.set_goal_position(dicts)

def get_pos():
    return dxl.get_present_position(tuple(fids)) #Tuple

dxl.enable_torque(fids)

print(motion("Book1.xlsx"))

dxl.disable_torque(fids)
