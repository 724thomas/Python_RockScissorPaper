
import time
import keyboard



def 동바산(i):
    time.sleep(1)
    if i in range(0, 14):
        keyboard.press_and_release('ctrl')
    elif i == 14:
        keyboard.press_and_release('f')
    elif i in range(15, 29):
        keyboard.press_and_release('ctrl')
    elif i == 29:
        keyboard.press_and_release('f')
    elif i in range(30, 45):
        keyboard.press_and_release('ctrl')
    elif i == 45:
        keyboard.press('left')
        time.sleep(0.7)
        keyboard.release('left')
        time.sleep(0.3)
        keyboard.press('right')
        time.sleep(1.4)
        keyboard.release('right')
    elif i == 46:
        keyboard.press_and_release('f')


while True:
    for i in range(46):
        if keyboard.is_pressed('e'):
            print('중지')
            exit()
        동바산(i)