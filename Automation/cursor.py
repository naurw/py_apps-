import pyautogui
import math
import time
from datetime import datetime 

# Radius 
R = 400
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius 
pyautogui.moveTo(X+R,Y)


running = True 
while running: 
    time.sleep(2)
    for i in range(360):
        # setting pace with a modulus 
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))


def run(): 
    running = True 
    while running: 
        time.sleep(2)
        if datetime.now().strftime('%H:%M:%S') != '17:10:30': 
            for i in range(360): 
                if i%6==0: 
                    pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))
        else: 
            return 

run()