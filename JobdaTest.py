
from PIL import ImageGrab, ImageOps
import winsound
from numpy import *
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import pyautogui
from skimage.feature import hog
import cv2
import numpy as np
from PIL import Image


def mousePos(cord):
    win32api.SetCursorPos( (cord[0], cord[1] ))
def 이미지구하기(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a
def 좌표구하기():
    alist=[]
    for i in range(2):
        while keyboard.is_pressed('e')==False:
            time.sleep(0.01)
        alist.append(get_realcords())
        winsound.Beep(600,200)
    trainColorGrab((alist[0][0],alist[0][1],alist[1][0],alist[1][1]))
    print("trainColorGrab(("+str(alist[0][0])+","+str(alist[0][1])+","+str(alist[1][0])+","+str(alist[1][1])+"))")
    time.sleep(2)
    trainColorGrab((alist[0][0],alist[0][1],alist[1][0],alist[1][1]))
    print("Center : " + str((alist[0][0]+alist[1][0])/2) + ", " + str((alist[0][1]+alist[1][1])/2))
def get_realcords():
    # while keyboard.is_pressed('q')==False:
    #     time.sleep(0.01)
    x,y = win32api.GetCursorPos()
    print (x,y)
    print("NleftClick("+str(x)+", "+str(y)+",2)")

def NleftClick(x,y,a):
    leftClick((x,y))
    time.sleep(a)
def leftClick(cord):
    win32api.SetCursorPos( (cord[0], cord[1] ))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def NrightClick(x,y,a):
    rightClick((x,y))
    time.sleep(a)
def NleftClick2(x,y,a):
    mousePos((x+2,y+2))
    time.sleep(0.1)
    mousePos((x-2,y-2))
    time.sleep(0.1)
    NleftClick(x,y,a)
def rightClick(cord):
    win32api.SetCursorPos( (cord[0], cord[1] ))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def trainColorGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im=ImageGrab.grab(box)
    return a
def trainGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im=ImageGrab.grab(box)
    return im
def get_ColorGrab():
    time.sleep(3)
    a= get_realcords()[0]
    b= get_realcords()[1]
    winsound.Beep(600,200)
    time.sleep(3)
    c= get_realcords()[0]
    d= get_realcords()[1]
    winsound.Beep(600,200)
    print ("trainColorGrab((" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "))"   )
    return trainGrab((a,b,c,d))


def trainHogGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    im = np.array(im)
    im = cv2.resize(im, (64, 64))  # Resize the image to a fixed size
    hog_features = hog(im, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
    return hog_features

def rsp():
    while True:
        if keyboard.is_pressed('e')==True:
                break
        mPaper = 36.48385936619978
        mScissors = 36.67819605668335
        mRock = 36.37207017184002
        mQuestion = 27.270559730902164

        yPaper = 35.57289837492688
        yScissors = 36.483946213222154
        yRock = 35.79645434762129
        yQuestion = 19.92130876371919

        im1 = sum(trainHogGrab((765,555,860,679))) #나
        im2 = sum(trainHogGrab((962,549,1073,686))) #상대

        if im1 != mQuestion:
            if im1 == mPaper: #나 보
                keyboard.press_and_release('down') #바위
            elif im1 == mScissors: #나 가위
                keyboard.press_and_release('right') #보
            elif im1 == mRock: #나 바위
                keyboard.press_and_release('left') #가위
        else:
            if im2 == yPaper: #상대 보
                keyboard.press_and_release('left') #가위
            elif im2 == yScissors: #상대 가위
                keyboard.press_and_release('down') #바위
            elif im2 == yRock: #상대 바위
                keyboard.press_and_release('right') #보

