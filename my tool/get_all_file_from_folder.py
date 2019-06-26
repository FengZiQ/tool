# coding=utf-8
import os
"""
遍历某个文件夹，列出该文件夹及子文件夹下的所有文件
"""


def traverse(f):
    all_file = []
    fs = os.listdir(f)
    for f1 in fs:
        tmp_path = os.path.join(f, f1)
        if not os.path.isdir(tmp_path):
            file = tmp_path.replace('\\', '/')
            print('文件: %s' % file)
            all_file.append(tmp_path.replace('\\', '/'))
        else:
            # print('文件夹：%s' % tmp_path)
            traverse(tmp_path)
    return all_file
