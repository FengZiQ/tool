# coding=utf-8
import sys
import re


class TextArea(object):
    def __init__(self):
        self.buffer = []

    def write(self, *args):
        self.buffer.append(args)


# 找到窗体坐标
def get_coordinate(window):
    coordinate = {}
    try:
        stdout = sys.stdout
        sys.stdout = TextArea()
        window.print_ctrl_ids()
        text_area, sys.stdout = sys.stdout, stdout
        temp = text_area.buffer[2][0]
        coordinate['left'] = int(re.findall('\(L(.+?), T', temp)[0])
        coordinate['top'] = int(re.findall('T(.+?), R', temp)[0])
        coordinate['right'] = int(re.findall('R(.+?), B', temp)[0])
        coordinate['bottom'] = int(re.findall('B(.+?)\)\n', temp)[0])
    except Exception as e:
        print('坐标定位失败！')
        print(e)

    return coordinate
