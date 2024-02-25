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
            # while keyboard.is_pressed('F7') == False:
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


def NF7Click(x, y, a):
    mousePos((x, y))
    키보드('v')
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


def 좌표구하기3():
    alist = []
    repeat = input()
    for i in range(int(repeat)):
        # while keyboard.is_pressed('e') == False:
        while keyboard.is_pressed('F7') == False:
            time.sleep(0.01)
        alist.append(temp())
        winsound.Beep(600, 200)


def temp():
    # while keyboard.is_pressed('q')==False:
    #     time.sleep(0.01)
    x, y = win32api.GetCursorPos()
    print("NF7Click(" + str(x) + ", " + str(y) + ",delay)")
    return [x, y]


def 키보드(key):
    keyboard.press_and_release(key)
    time.sleep(0.01)


def 종료와재접():
    NleftClick(820, 1052, 1)
    NleftClick(966, 545, 5)
    while trainColorGrab((1663, 953, 1877, 1016)) == 13482:
        time.sleep(1)
    time.sleep(5)

    NleftClick(1043, 993, 2)
    while trainColorGrab((1663, 953, 1877, 1016)) == 13482:
        time.sleep(1)
    time.sleep(5)


def 곰변신():
    키보드("w")
    NrightClick(958, 586, 2)
    키보드("w")


def 콜드플레인사냥(time):
    delay = time
    NF7Click(1850, 903, delay+0.2)
    NF7Click(1849, 903, delay+0.2)
    NF7Click(1849, 901, delay+0.2)
    NF7Click(1849, 901, delay+0.2)
    NF7Click(1795, 922, delay+0.2)
    NF7Click(1829, 739, delay+0.2)
    NF7Click(1840, 707, delay+0.2)
    NF7Click(541, 885, delay+0.2)
    NF7Click(0, 886, delay+0.2)
    NF7Click(23, 849, delay+0.2)
    NF7Click(46, 717, delay)
    NF7Click(1667, 768, delay)
    NF7Click(1822, 733, delay)
    NF7Click(1818, 773, delay)
    NF7Click(1822, 768, delay)
    NF7Click(1780, 790, delay)
    NF7Click(232, 882, delay)
    NF7Click(793, 913, delay)
    NF7Click(1666, 766, delay)
    NF7Click(1775, 591, delay)
    NF7Click(1766, 301, delay)
    NF7Click(1805, 187, delay)
    NF7Click(1803, 190, delay)
    NF7Click(1788, 136, delay)
    NF7Click(1777, 67, delay)
    NF7Click(795, 0, delay)
    NF7Click(309, 0, delay)
    NF7Click(289, 5, delay)
    NF7Click(343, 0, delay)
    NF7Click(342, 1, delay)
    NF7Click(1484, 222, delay)
    NF7Click(1769, 663, delay)
    NF7Click(1796, 720, delay)
    NF7Click(1774, 164, delay)
    NF7Click(1561, 8, delay)
    NF7Click(621, 0, delay)
    NF7Click(469, 21, delay)
    NF7Click(692, 0, delay)
    NF7Click(1651, 85, delay)
    NF7Click(1811, 986, delay)
    NF7Click(1799, 978, delay)
    NF7Click(1820, 835, delay)
    NF7Click(1789, 848, delay)
    NF7Click(1774, 869, delay)
    NF7Click(1720, 898, delay)
    NF7Click(626, 886, delay)
    NF7Click(1424, 0, delay)
    NF7Click(1616, 0, delay)
    NF7Click(1613, 1, delay)
    NF7Click(1529, 0, delay)
    NF7Click(628, 0, delay)
    NF7Click(959, 5, delay)
    NF7Click(1735, 526, delay)
    NF7Click(1788, 917, delay)
    NF7Click(1766, 874, delay)
    NF7Click(1790, 427, delay)
    NF7Click(1699, 205, delay)
    NF7Click(1477, 0, delay)
    NF7Click(1520, 25, delay)
    NF7Click(146, 67, delay)
    NF7Click(341, 215, delay)
    NF7Click(1842, 139, delay)
    NF7Click(1779, 367, delay)
    NF7Click(1780, 712, delay)
    NF7Click(1522, 896, delay)
    NF7Click(490, 0, delay)
    NF7Click(837, 0, delay)
    NF7Click(1532, 47, delay)
    NF7Click(1713, 244, delay)
    NF7Click(1483, 168, delay)
    NF7Click(1647, 629, delay)
    NF7Click(1676, 895, delay)
    NF7Click(1743, 890, delay)
    NF7Click(1751, 911, delay)
    NF7Click(1750, 913, delay)
    NF7Click(1748, 917, delay)
    NF7Click(1748, 917, delay)
    NF7Click(1748, 917, delay)
    NF7Click(1738, 922, delay)
    NF7Click(1738, 922, delay)
    NF7Click(1784, 859, delay)
    NF7Click(0, 277, delay)
    NF7Click(0, 268, delay)
    NF7Click(0, 499, delay)
    NF7Click(0, 643, delay)
    NF7Click(31, 835, delay)
    NF7Click(345, 868, delay)
    NF7Click(928, 881, delay)
    NF7Click(1573, 880, delay)
    NF7Click(1550, 835, delay)
    NF7Click(1160, 886, delay)
    NF7Click(1720, 678, delay)
    NF7Click(0, 885, delay)
    NF7Click(22, 861, delay)
    NF7Click(364, 891, delay)
    NF7Click(0, 412, delay)
    NF7Click(7, 677, delay)
    NF7Click(70, 829, delay)
    NF7Click(120, 800, delay)
    NF7Click(676, 0, delay)
    NF7Click(567, 41, delay)
    NF7Click(1086, 0, delay)
    NF7Click(1806, 43, delay)
    NF7Click(1815, 293, delay)
    NF7Click(1661, 0, delay)
    NF7Click(1652, 0, delay)
    NF7Click(809, 80, delay)
    NF7Click(344, 508, delay)
    NF7Click(164, 896, delay)
    NF7Click(115, 840, delay)
    NF7Click(114, 473, delay)
    NF7Click(24, 665, delay)
    NF7Click(39, 645, delay)
    NF7Click(1839, 0, delay)
    NF7Click(1565, 106, delay)
    NF7Click(1280, 48, delay)


print("Start")
# 좌표구하기2()
# 좌표구하기3()

time.sleep(2)
for i in range(1000):
    print(i)
    종료와재접()
    곰변신()
    콜드플레인사냥(0.3)
    time.sleep(1)
for _ in range(10):
    winsound.Beep(600, 200)

# 콜드 플레인
# 0.5: 557 1891 -> 2452
# 1.0: 359 2452 -> 2811
# 블러드 무어
# 0.5: 345
