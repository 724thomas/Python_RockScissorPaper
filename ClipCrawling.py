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


# time.sleep(2)
# get_realcords()


def toggleJavaScript():  # 자바스크립트 토글
    NleftClick(1464, 754, 0.5)


def saveClip(directory):  # 우클릭후 다른 이름으로 저장
    NrightClick(501, 610, 2)
    NleftClick(585, 703, 2)
    NleftClick(1518, 46, 2)  # URL창 클릭

    subdirectory = changeName(input("subdirectory(Part) :"))
    subsubdirectory = changeName(input("subsubdirectory(Chapter) :"))
    saveDetail(directory, subdirectory, subsubdirectory)

    keyboard.press_and_release('enter')
    time.sleep(2)


def changeName(string):
    while "." in string:  # .이 있을때
        string = string.replace(".", "")
    while ":" in string:  # : 이 있을때
        string = string.replace(":", "")
    while "?" in string:
        string = string.replace("?", "")
    while "!" in string:
        string = string.replace("!", "")
    while "," in string:
        string = string.replace(",", "")
    while string[-1] in "0123456789:":  # 마지막 글자가 숫자나 : 일때
        string = string[:-1]
    return string


def createFolder(save_directory, title, sub_directory, sub_sub_directory):
    try:
        final_folder = save_directory + "\\" + title + "\\" + sub_directory + "\\" + sub_sub_directory
        if not os.path.exists(final_folder):
            os.makedirs(final_folder)
    except OSError:
        print('Error: Creating directory. ' + final_folder)
    return final_folder


def saveDetail(directory, subdirectory, subsubdirectory):  # 저장할 폴더 이름 입력

    filenames = []
    for i in range(input("몇개의 파일인가요?")):
        filenames.append(changeName(input("파일 이름을 입력하세요 : ")) + ".mp4")

    NrightClick(501, 610, 2)
    NleftClick(585, 703, 2)

    NleftClick(1518, 46, 2)  # URL창 클릭

    createFolder(directory, subdirectory, subsubdirectory)
    finaldirectory = directory + "\\" + subdirectory + "\\" + subsubdirectory
    print("Current Directory : " + finaldirectory)

    NleftClick(1380, 436, 2)  # 파일 이름 입력창 클릭
    keyboard.write(finaldirectory)
    return finaldirectory


# saveClip("E:\패스트캠퍼스 강의\올인원 패키지, 만들면서 익히는 React의 모든 것 개발부터 배포까지 with 25개 스택")


def nextClip():  # 다음 클립으로 넘어가기
    mousePos((900, 993))
    time.sleep(0.5)
    NleftClick(156, 1061, 2)
    time.sleep(5)


def all_in_one():
    save_directory = "E:\패스트캠퍼스 강의"
    # 영상 큰 제목 입력
    directory = changeName(input("title : "))
    # 영상 작은 제목 입력
    sub_directory = changeName(input("subdirectory(Part) : "))
    # 영상 작은 제목 입력
    sub_sub_directory = changeName(input("subsubdirectory(Chapter) : "))
    final_directory = createFolder(save_directory, directory, sub_directory, sub_sub_directory)

    # 파일 갯수 입력
    filenames = []
    for i in range(int(input("몇개의 파일인가요?"))):
        # 파일 이름 입력
        filenames.append(changeName(input("파일 이름을 입력하세요 : ")) + ".mp4")

    time.sleep(10)

    for i in range(len(filenames)):
        # Disbale JavaScript
        toggleJavaScript()
        time.sleep(1)

        NrightClick(501, 610, 2)
        NleftClick(585, 703, 2)

        while trainColorGrab((12, 8, 147, 26)) not in (19209, 18376):
            time.sleep(1)
        time.sleep(1)

        NleftClick(1518, 46, 2)  # URL창 클릭
        keyboard.write(final_directory)
        time.sleep(0.5)
        keyboard.press_and_release('enter')

        NleftClick(1380, 436, 2)  # 파일 이름 입력창 클릭
        keyboard.write(filenames[i])
        time.sleep(0.5)
        keyboard.press_and_release('enter')
        time.sleep(1)

        toggleJavaScript()
        time.sleep(1)
        nextClip()
        time.sleep(3)
        NleftClick(621,625,2)
        time.sleep(3)

all_in_one()
# 좌표구하기2()
