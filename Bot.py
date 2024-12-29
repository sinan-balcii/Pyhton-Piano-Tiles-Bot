from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Title 1 Position: X:  353 Y:  400 RGB: (  0,   0,   0)
#Title 2 Position: X:  412 Y:  400 RGB: (  0,   0,   0)
#Title 3 Position: X:  528 Y:  400 RGB: (178, 182, 234)
#Title 4 Position: X:  592 Y:  400 RGB: (184, 188, 235)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('c') == False:
    while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(519, 400) [0] == 0: 
            click(519, 400)
  

        if pyautogui.pixel(639, 400) [0] == 0:
            click(639, 400)
       

        if pyautogui.pixel(716, 400) [0] == 0: 
            click(716, 400)


        if pyautogui.pixel(796, 400) [0] == 0: 
            click(796, 400)


    break
            
