import RPi.GPIO as RP
from time import sleep
from os import system
from pynput import keyboard as Keys

Servo = [7, 12, 16, 20, 21]

RP.setmode(RP.BCM)
RP.setwarnings(False)

for i in Servo:
    RP.setup(i,RP.OUT)

class datas:
    Page=0
    servnum=0
    deg=''

ServoKey=[['left','right'],['down','up'],['0','2'],['5','8'],['7','9']]
pwm=[]
TS=[]

for i in range(0,len(Servo)):
    TS.append(90)
    pwm.append(RP.PWM(Servo[i],50))
    pwm[i].start(ferq(90))

def ferq(degre):
    return 2.6 + ((degre - 1) * 0.0559)

def home():
    st='╔'
    for a in range(0,len(TS)):
        st+='═'*10
        for b in str(TS[a]):
            st+='═'
        st+='╦'
    st=st[0:len(st)-1]+'╗\n'
    for i in range(0,len(TS)):
        st+='║ Servo{}: {} '.format(i+1,str(TS[i]))
    st+='║\n╚'
    for a in range(0,len(TS)):
        st+='═'*10
        for b in str(TS[a]):
            st+='═'
        st+='╩'
    st=st[0:len(st)-1]+'╝\n'
    st+=('Quit <esc>\n')
    system('clear')
    print(st,end='',flush=True)

def set(key):
    for a in range(0,len(ServoKey)):
        for b in range(0,len(ServoKey[0])):
            if ServoKey[a][b]==key:
                if (b): 
                    if(TS[a]<180):
                        TS[a]+=1
                else:
                    if(TS[a]>0):
                        TS[a]-=1
                pwm[a].ChangeDutyCycle(ferq(TS[a]))
                home()
def on_press(key):
    try:
        set(str(key.char))
    except AttributeError:
        set(str(key).split('.')[1])
def on_release(key):
    if key == Keys.Key.esc:
        for pwmx in pwm:
            pwmx.stop()
        RP.cleanup()
        return False
home()
with Keys.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
