# coding=utf-8
import requests
import socket
import time

"""
线上dm对应的三个结点：
114.215.31.105
139.129.209.77
118.190.78.254
"""
hostIp = 'http://dm.inspos.cn'
count = 1
ip105 = 0
ip77 = 0
ip254 = 0

for i in range(100):
    ip = socket.gethostbyname(hostIp.replace('http://', ''))
    res = requests.get(hostIp)

    if '登录' in res.text:
        print('\n第%d次请求成功'%count)
        print(ip)
        print('响应时长为：%s'%str(res.elapsed.total_seconds()))
        if ip == '114.215.31.105':
            ip105 += 1
        elif ip == '139.129.209.77':
            ip77 += 1
        elif ip == '118.190.78.254':
            ip254 += 1
    else:
        print('\n第%d次请求失败'%count)
    res.close()
    count += 1
    time.sleep(1)

print('114.215.31.105结点出现了%d次'%ip105)
print('139.129.209.77结点出现了%d次'%ip77)
print('118.190.78.254结点出现了%d次'%ip254)