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
    while "/" in string:
        string = string.replace("/", "")
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
    time.sleep(2)


def all_in_one(save_directory, title, part, chapter, filenames):
    final_directory = createFolder(save_directory, title, part, chapter)

    for i in range(len(filenames)):
        toggleJavaScript()  # Disbale JavaScript
        time.sleep(1)

        NrightClick(672, 514, 2)  # 우클릭
        NleftClick(762, 597, 2)  # 다른 이름으로 저장

        # while trainColorGrab((12, 8, 147, 26)) not in (19209, 18376, 18699):
        while trainColorGrab((10, 6, 30, 21)) not in (0, 13945):
            time.sleep(1)
        time.sleep(1)

        NleftClick(1518, 46, 2)  # URL창 클릭
        keyboard.write(final_directory)
        time.sleep(0.5)
        keyboard.press_and_release('enter')

        # NleftClick(1380, 436, 2)  # 파일 이름 입력창 클릭
        NleftClick(1254, 980, 2)
        keyboard.write(filenames[i])
        time.sleep(0.5)
        keyboard.press_and_release('enter')
        time.sleep(1)

        toggleJavaScript()  # Enable JavaScript
        time.sleep(1)
        nextClip()
        time.sleep(2)
        NleftClick(621, 625, 2)
        print("Saved " + filenames[i] + " in " + final_directory)
        time.sleep(3)


def chapter_all_in_one(save_directory):
    # 영상 큰 제목 입력
    title = changeName(input("title : "))
    # 영상 작은 제목 입력
    part = changeName(input("subdirectory(Part) : "))
    # 영상 작은 제목 입력
    chapters = []
    filenames = []
    for i in range(int(input("몇개의 챕터인가요?"))):
        chapters.append(changeName(input("챕터 이름을 입력하세요 : ")))
        chapter_file = []
        for j in range(int(input("몇개의 파일인가요?"))):
            chapter_file.append(changeName(input("파일 이름을 입력하세요 : ")) + ".mp4")
        filenames.append(chapter_file)
        print("")

    time.sleep(10)

    for i in range(len(chapters)):
        print("Current Directory : " + save_directory + "\\" + title + "\\" + part + "\\" + chapters[i])
        print(filenames[i])
        all_in_one(save_directory, title, part, chapters[i], filenames[i])


def part_all_in_one():
    save_directory = "E:\패스트캠퍼스 강의"
    # 영상 큰 제목 입력
    title = changeName(input("title : "))
    all_parts_chapters_filenames = []

    for i in range(int(input("몇개의 파트인가요?"))):
        part = changeName(input("subdirectory(Part) : "))
        for j in range(int(input("몇개의 챕터인가요?"))):
            chapter = changeName(input("subsubdirectory(Chapter) : "))
            file_names = []
            for k in range(int(input("몇개의 파일인가요?"))):
                file_names.append(changeName(input("파일 이름을 입력하세요 : ")) + ".mp4")
                print("")
            print("")

            all_parts_chapters_filenames.append([part, chapter, file_names])

    time.sleep(10)

    for part, chapter, file_names in all_parts_chapters_filenames:
        # print([part, chapter, file_names])
        all_in_one(save_directory, title, part, chapter, file_names)


# part_all_in_one()

# trainColorGrab((48,251,544,273))
# time.sleep(0.5)
# 좌표구하기2()
# trainColorGrab((0,252,187,277))

# while trainColorGrab((48, 251, 544, 273)) not in range(17865, 17875):
#     if keyboard.is_pressed('e') == True:
#         break
#     NleftClick(752, 783, 0.1)
#     mousePos((40, 138))
#     # mousePos((130, 286))
#     mousePos((30, 186))
#     time.sleep(0.1)
#
#
# '''
# mousePos((30, 186))
# mousePos((40, 138))

def change_bag(x, y):
    mousePos((780, 712))
    NleftClick(781, 713, 1)
    NleftClick(x, y, 1)
    NleftClick(781, 713, 1)
    same_count = 0


def all_res_LC():
    count = 0
    same_count = 0
    bag_idx = 0
    same_check = 0
    shimmering = -1
    while True or count < 9:
        y = [1420, 1470, 1520, 1570, 1620, 1670, 1720, 1770, 1820, 1870]
        deposit_x = 434
        take_out_x = 730
        bag_x = 514
        # while trainColorGrab((12,282,501,308)) != 54917:
        # 21709 , 10795
        # while not (shimmering == 21709 and trainColorGrab((65, 199, 238, 226)) in (0, 1)):
        while shimmering != 19622 or trainColorGrab((9, 203, 490, 225)) != 17422:
            # while not (shimmering == 21709
            shimmering = trainColorGrab((9, 203, 590, 225))
            if shimmering == same_check:
                same_count += 1
                print("same", same_count)
                if same_count == 15:
                    print("depleted")
                    change_bag(y[bag_idx], bag_x)
                    bag_idx += 1
                    same_count = 0
            else:
                same_count = 0
                same_check = shimmering

            if keyboard.is_pressed('e') == True:
                break
            NleftClick(752, 783, 0.03)
            mousePos((30, 186))
            mousePos((40, 138))
            time.sleep(0.05)

        if keyboard.is_pressed('e') == True:
            break

        NleftClick(43, 170, 1)
        NleftClick(y[count], take_out_x, 1)
        count += 1
        NleftClick(y[count], deposit_x, 1)
        NleftClick(43, 170, 1)
        NleftClick(752, 783, 0.03)
        mousePos((30, 186))
        mousePos((40, 138))
        shimmering = trainColorGrab((16, 201, 597, 225))
        # '''


def jewelIASAR():
    while True:
        # while trainColorGrab((569,232,599,419)) in range(8510, 8530):
        #     if keyboard.is_pressed('e') == True:
        #         break
        #     NleftClick(752, 783, 0.1)
        #     mousePos((40, 138))
        #     mousePos((30, 186))
        #     time.sleep(0.1)
        # while trainColorGrab((0,252,187,277)) not in (11444,11273) or trainColorGrab((517,230,551,411)) in range(9063, 9067):
        while trainColorGrab((538, 459, 794, 483)) != 13329 or trainColorGrab((583, 534, 791, 561)) != 13000:
            if keyboard.is_pressed('e') == True:
                break
            NleftClick(752, 783, 0.04)
            mousePos((768, 664))
            mousePos((780, 664))
            time.sleep(0.05)
        if keyboard.is_pressed('e') == True:
            break


def find_set():
    while True:
        if keyboard.is_pressed('e') == True:
            break
        elif keyboard.is_pressed('w') == True:
            x, y = win32api.GetCursorPos()
            NleftClick(x, y, 0.05)
            NleftClick(1444, 433, 0.05)
            NrightClick(1444, 433, 0.05)
            NleftClick(757, 783, 0.05)
            # NleftClick(163, 143, 0.05)
            NleftClick(265, 148, 0.05)
            keyboard.press_and_release('esc')
            NleftClick(x, y, 0.05)
            mousePos((x + 99, y))
            time.sleep(0.05)


def find_cd_ias_jewwl():
    while True:
        if keyboard.is_pressed('e') == True:
            break
        if trainColorGrab((571, 453, 784, 474)) == 10262 and trainColorGrab((579, 535, 784, 565)) == 13534:
            NleftClick(779, 664, 1)
            NleftClick(46, 118, 1)
            if trainColorGrab((338, 213, 392, 237)) not in (0, 10486, 6647):
                break
        else:
            NleftClick(763, 789, 0.02)
            mousePos((779, 664))
            time.sleep(0.05)
    for _ in range(3):
        winsound.Beep(600, 200)


def qol_stack():
    while True:
        if keyboard.is_pressed('+') == True:
            keyboard.press_and_release('u')
            x = 1416
            y = 410
            diff = 49
            time.sleep(0.3)
            keyboard.press("ctrl")
            for i in range(6):
                for j in range(4):
                    # mousePos(((x-5)+(i*diff), (y-5)+(j*diff), (x+5)+(i*diff), (y+5)+(j*diff)))
                    item = trainColorGrab(
                        ((x - 5) + (i * diff), (y - 5) + (j * diff), (x + 5) + (i * diff), (y + 5) + (j * diff)))
                    if item != 107:
                        NleftClick(x + (i * diff), y + (j * diff), 0.05)
                        NleftClick(757, 790, 0.05)
            keyboard.release("ctrl")
            keyboard.press_and_release('esc')


# trainColorGrab((538,459,794,483))
# change_bag(1420, 514)
# trainColorGrab((16, 201, 597, 225)) #21670
# trainColorGrab((65, 199, 238, 226)) # 10795):

# trainColorGrab((9, 203, 590, 225))
# trainColorGrab((9, 203, 490, 225))
all_res_LC()
# 좌표구하기()
# trainColorGrab((15, 207, 449, 312))
# jewelIASAR()
# time.sleep(2)
# find_cd_ias_jewwl()

# qol_stack()

# mousePos((1177, 386))
# 좌표구하기()


def javGC():
    while True:
        # while trainColorGrab((569,232,599,419)) in range(8510, 8530):
        #     if keyboard.is_pressed('e') == True:
        #         break
        #     NleftClick(752, 783, 0.1)
        #     mousePos((40, 138))
        #     mousePos((30, 186))
        #     time.sleep(0.1)
        # while trainColorGrab((0,252,187,277)) not in (11444,11273) or trainColorGrab((517,230,551,411)) in range(9063, 9067):
        while trainColorGrab((8, 251, 400, 279)) != 18033:
            if keyboard.is_pressed('e') == True:
                break
            NleftClick(752, 783, 0.03)
            mousePos((40, 138))
            mousePos((30, 186))
            time.sleep(0.05)
        if keyboard.is_pressed('e') == True:
            break


def amul():
    # keyboard.press_and_release('i')
    # time.sleep(0.2)
    NrightClick(1834, 728, 1)
    for i in range(7):
        큐브넣기(1421, 460 + (i * 49))
        NleftClick(757, 790, 0.05)
        keyboard.press("ctrl")
        NleftClick(781, 711, 0.05)
        keyboard.release("ctrl")
    for i in range(8):
        큐브넣기(1616, 408 + (i * 49))
        NleftClick(757, 790, 0.05)
        keyboard.press("ctrl")
        NleftClick(781, 711, 0.05)
        keyboard.release("ctrl")


def 큐브넣기(x, y):
    keyboard.press("ctrl")
    for i in range(4):
        NleftClick(x + (i * 49), y, 0.05)
    keyboard.release("ctrl")

def 종료와재접(x):
    NleftClick(820, 1052, 1)
    NleftClick(966, 545, 2)
    while trainColorGrab((1663, 953, 1877, 1016)) == 13482:
        time.sleep(1)
    time.sleep(2)

    for i in range(x):
        keyboard.press_and_release('down')
        time.sleep(0.05)
    NleftClick(1043, 993, 2)
    while trainColorGrab((1663, 953, 1877, 1016)) == 13482:
        time.sleep(1)
    time.sleep(2)

def 창고가기():
    mousePos((888, 257))
    time.sleep(0.01)
    mousePos((890, 259))
    time.sleep(0.01)
    NleftClick(889, 258,0.01)
    NleftClick(889, 258,3)
    NleftClick(760, 93,3)

def 창고로옮기기():
    keyboard.press("ctrl")
    for i in range(7):
        NleftClick(1421+(49*3), 460 + (i * 49), 0.05)
    for i in range(8):
        NleftClick(1616+(49*3), 408 + (i * 49), 0.05)
    keyboard.release("ctrl")

# while True:
#     if keyboard.is_pressed('+') == True:
#         for _ in range(10):
#             종료와재접(11)
#             창고가기()
#             amul()
#             keyboard.press_and_release('esc')
#             창고로옮기기()
#     elif keyboard.is_pressed('-') == True:
#         keyboard.press("ctrl")
#         for i in range(8):
#             for j in range(8):
#                 NleftClick(1418+(i*49), 413+(j*49),0.05)
#         keyboard.release("ctrl")
#     time.sleep(0.05)

# 좌표구하기()
# 큐브넣기(1421,559)
# 창고가기()
# 종료와재접(9)