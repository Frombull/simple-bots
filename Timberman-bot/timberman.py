from keyboard import is_pressed
from pyautogui import pixel
import win32api, win32con
from time import sleep


'''
Game link: https://play.famobi.com/timber-man
'''


KEYS = {
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28
}


def press(button):
    win32api.keybd_event(KEYS[button], 0, 0, 0)
    sleep(0.006)
    win32api.keybd_event(KEYS[button], 0, win32con.KEYEVENTF_KEYUP, 0)


def main():
    while not is_pressed('q'):
        if pixel(878, 578)[0] < 200:
            press('right_arrow')
        else:
            press('left_arrow')


if __name__ == '__main__':
    sleep(2)
    main()
