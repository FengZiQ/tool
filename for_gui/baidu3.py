# coding=utf-8
import threading
import os

cases_list = ['baidu1.py', 'baidu2.py']


def execute_case(case):
    os.system('python ' + case)


for case in cases_list:
    t = threading.Thread(target=execute_case, args=(case,))
    t.start()
    execute_case(case)
