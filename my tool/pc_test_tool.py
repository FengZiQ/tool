# coding=utf-8
from findCoordinate import get_coordinate
import pyautogui
import time


# 点击操作
def click_action(window, left, top):
    wcl = get_coordinate(window)
    pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
    pyautogui.click()
    time.sleep(2)
    return


# 鼠标悬停
def mouse_over(window, left, top):
    wcl = get_coordinate(window)
    pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
    time.sleep(2)
    return


# 填充文本框操作0
def fill_in_text(window, left, top, text):
    wcl = get_coordinate(window)
    pyautogui.moveTo(wcl['left'] + left, wcl['top'] + top)
    pyautogui.click()
    pyautogui.typewrite(text)
    time.sleep(1)
    return


