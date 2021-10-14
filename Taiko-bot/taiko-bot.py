from keyboard import is_pressed
import win32api, win32con
import pyautogui as pygui
from time import sleep


KEYS = {
    'j': 0x4A,
    'k': 0x4B,
    'f': 0x46,
    'd': 0x44
}


def press(button):
    win32api.keybd_event(KEYS[button], 0, 0, 0)
    sleep(0.06)
    win32api.keybd_event(KEYS[button], 0, win32con.KEYEVENTF_KEYUP, 0)


def main():
    while not is_pressed('q'):
        #Red circle
        if pygui.pixelMatchesColor(615, 370, (247, 74, 32), tolerance=3):
            press('j')
        
        #Blue circle
        elif pygui.pixelMatchesColor(615, 375, (50, 173, 189), tolerance=3):
            press('k')
        
        #Yellow bar
        elif pygui.pixelMatchesColor(615, 375, (255, 180, 0), tolerance=3):
            press('j')
            sleep(0.02)
            press('f')

        #Baloon
        elif pygui.pixelMatchesColor(920, 463, (255, 148, 24), tolerance=3):
            press('j')
            sleep(0.02)
            press('f')


if __name__ == '__main__':
    sleep(2)
    main()
