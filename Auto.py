import os
from time import sleep as sl

t = input('Enter Time: [s/m/h] ')
t = str(t)

if t.endswith('s'):
    t = t.replace('s', '')
    try:
        t = int(t)
    except:
        t = float(t)
    sl(t)
    print(t)
    os.system("shutdown /s /t 0")
if t.endswith('m'):
    t = t.replace('m', '')
    try:
        t = int(t)
    except:
        t = float(t)
    t = t * 60
    sl(t)
    print(t)
    os.system("shutdown /s /t 0")
if t.endswith('h'):
    t = t.replace('h', '')
    try:
        t = int(t)
    except:
        t = float(t)
    t = t * 3600
    sl(t)
    print(t)
    os.system("shutdown /s /t 0")