from keyboard import is_pressed
from pyautogui import pixel
import win32api, win32con
from time import sleep


'''
Game link: https://www.ojogos.com.br/jogo/teclas-de-piano-magicas
'''


def click(x: int, y: int):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def main():
    tiles_y = 850
    tiles = {
        't1_x': 770,
        't2_x': 910,
        't3_x': 1050,
        't4_x': 1190
    }

    while not is_pressed('q'):
        if pixel(tiles['t1_x'], tiles_y)[0] == 0:
            click(tiles['t1_x'], tiles_y)

        elif pixel(tiles['t2_x'], tiles_y)[0] == 0:
            click(tiles['t2_x'], tiles_y)

        elif pixel(tiles['t3_x'], tiles_y)[0] == 0:
            click(tiles['t3_x'], tiles_y)

        elif pixel(tiles['t4_x'], tiles_y)[0] == 0:
            click(tiles['t4_x'], tiles_y)


if __name__ == '__main__':
    main()
