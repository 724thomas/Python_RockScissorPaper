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
    win32api.SetCursorPos((cord[0], cord[1]))


def 이미지구하기(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    return a


def 좌표구하기():
    alist = []
    repeat = input()
    for i in range(int(repeat)):
        while keyboard.is_pressed('e') == False:
            time.sleep(0.01)
        alist.append(get_realcords())
        winsound.Beep(600, 200)


def 드래그드랍(x, y, x2, y2, sleeptime):
    mousePos((x, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    mousePos((x2, y2))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)
    time.sleep(sleeptime)


def 좌표구하기2():
    alist = []
    for i in range(2):
        while keyboard.is_pressed('e') == False:
            time.sleep(0.01)
        alist.append(get_realcords())
        winsound.Beep(600, 200)
    trainColorGrab((alist[0][0], alist[0][1], alist[1][0], alist[1][1]))
    print("trainColorGrab((" + str(alist[0][0]) + "," + str(alist[0][1]) + "," + str(alist[1][0]) + "," + str(
        alist[1][1]) + "))")
    print("Center : " + str((alist[0][0] + alist[1][0]) / 2) + ", " + str((alist[0][1] + alist[1][1]) / 2))


def get_realcords():
    # while keyboard.is_pressed('q')==False:
    #     time.sleep(0.01)
    x, y = win32api.GetCursorPos()
    print(x, y)
    print("NleftClick(" + str(x) + ", " + str(y) + ",2)")
    return [x, y]


def NleftClick(x, y, a):
    leftClick((x, y))
    time.sleep(a)


def leftClick(cord):
    win32api.SetCursorPos((cord[0], cord[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# while True:
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     time.sleep(.01)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#     time.sleep(1)
def NrightClick(x, y, a):
    rightClick((x, y))
    time.sleep(a)


def NleftClick2(x, y, a):
    mousePos((x + 2, y + 2))
    time.sleep(0.1)
    mousePos((x - 2, y - 2))
    time.sleep(0.1)
    NleftClick(x, y, a)


def rightClick(cord):
    win32api.SetCursorPos((cord[0], cord[1]))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)


def trainColorGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im = ImageGrab.grab(box)
    return a


def trainGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im = ImageGrab.grab(box)
    return im


def get_ColorGrab():
    time.sleep(3)
    a = get_realcords()[0]
    b = get_realcords()[1]
    winsound.Beep(600, 200)
    time.sleep(3)
    c = get_realcords()[0]
    d = get_realcords()[1]
    winsound.Beep(600, 200)
    print("trainColorGrab((" + str(a) + "," + str(b) + "," + str(c) + "," + str(d) + "))")
    return trainGrab((a, b, c, d))


def trainHogGrab(cords):
    box = (cords)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    im = np.array(im)
    im = cv2.resize(im, (64, 64))  # Resize the image to a fixed size
    hog_features = hog(im, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1))
    return hog_features


##################################################################################################################
def enchant():
    NleftClick(925, 990, 2)
    NleftClick(936, 416, 2)


def center():
    NleftClick(968, 475, 0.5)

def timeclock():
    NleftClick(927, 669,0.5)

def checkDeath():
    return True if trainColorGrab((173, 158, 367, 355)) in range(38000, 38300) else False





def die():
    NleftClick(1172, 996, 0.5)
    NleftClick(1013, 204, 0.5)
    NleftClick(933, 548, 0.1)
    NleftClick(933, 548, 0.1)
    NleftClick(933, 548, 0.1)


def can_enchant():
    a = trainColorGrab((899, 965, 961, 982))
    print(a)
    return False if a in range(2345, 2355) or a in range(2295, 2309) else True #range(1350, 1370)
    #2348 : reclaiming , #2302 : not enough level

def enchant_and_research():
    while not can_enchant():
        time.sleep(1)
    NleftClick(924, 992, 1)
    NleftClick(933, 417, 1)
    NleftClick(924, 992, 1)
    time.sleep(4)


def idle(x, y, d=10):
    num_enchant = 0
    while True:
        death = 0
        waiting = 0
        # while waiting <= 1200 and death <= d:
        # while waiting <= 0 and death <= d:
        while death <= d:
            time.sleep(1)
            waiting += 1
            print("waiting : " + str(waiting))
            print("enchant : " + str(num_enchant) + " times")
            print("death : " + str(death) + " times")
            if checkDeath():
                death += 1
                print("death : " + str(death))
                for i in range(15):
                    # center()
                    timeclock()
                time.sleep(3)
                print("checking perk...")
                if x!=0 and y!=0:
                    perkUp(x, y)
                time.sleep(3)
                waiting = 0
        if can_enchant():
            enchant()
        num_enchant += 1


def test():
    die()
    time.sleep(6)
    NleftClick(1085, 273,0.5)
    NleftClick(784, 499,0.1)
    NleftClick(846, 496,0.1)
    NleftClick(857, 268,0.5)
    NleftClick(783, 525,0.1)
    NleftClick(777, 273,0.5)
    NleftClick(783, 555,0.5)
    NleftClick(927, 285,0.1)

    NleftClick(774, 928, 0.5)
    드래그드랍(744, 427, 815, 241, 0.1)
    드래그드랍(818, 427, 895, 231, 0.1)
    드래그드랍(894, 423, 969, 246, 0.1)
    드래그드랍(965, 432, 1041, 241, 0.1)
    NleftClick(779, 916, 0.5)
    time.sleep(15)
    for i in range(3):
        enchant_and_research()
        print(str(i) + "번째")
        time.sleep(10)


def perkUp(x, y):
    if trainColorGrab((666, 968, 732, 986)) not in range(3010, 3030): #(3280, 3284):
        NleftClick(666, 968, 2)

        slot1 = trainColorGrab((820, 357, 880, 370))  # 1슬롯
        slot2 = trainColorGrab((820 + 77, 357, 880 + 77, 370))  # 2슬롯
        slot3 = trainColorGrab((820 + 154, 357, 880 + 154, 370))  # 3슬롯
        if slot1 in range(x-5, x+5) or slot1 in range(y-5, y+5):
            print("slot1 match")
            NleftClick(853, 361, 2)
        elif slot2 in range(x-5, x+5) or slot2 in range(y-5, y+5):
            print("slot2 match")
            NleftClick(930, 361, 2)
        elif slot3 in range(x-5, x+5) or slot3 in range(y-5, y+5):
            print("slot3 match")
            NleftClick(1007, 361, 2)
        else:
            print("no match")
            NleftClick(853, 361, 2)
        perkselect()

def perkselect():
    for i in range(11):
        NleftClick(936, 738 + (i * 30), 0.2)
    NleftClick(925, 1065, 2)

# perkUp(1840, 1906)
# perkUp(1610,1254)
# while True:
#     test()
# idle(1840, 1906, 10)
# idle(1081, 1383, 10)
# idle(1254, 1610, 10)
# idle(2173, 1758, 20)
idle(2173, 1400, 5)

# while True:
#     if can_enchant():
#         enchant()
#     time.sleep(3)

# while True:
#     perkUp(1462,1212)
#     time.sleep(3)
trainColorGrab((820, 357, 880, 370))
trainColorGrab((820+77, 357, 880+77, 370))
trainColorGrab((820+154, 357, 880+154, 370))

# while True:
#     trainColorGrab((899,965,961,982))


#
# get_ColorGrab()
# 좌표구하기()

