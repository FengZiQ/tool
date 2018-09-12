# coding=utf-8
import paramiko
import time


def send_cmd(cmd):
    server = 'nexus.2dupay.com'
    username = 'yingying'
    pwd = 'zhaxinbu666'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server, username=username, password=pwd)
    c = ssh.invoke_shell()
    result = {'data': ''}
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        if result['data']:
            c.send(cmd + '\n')
            time.sleep(2)
            break

    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        if result['data']:
            break
    if result['data'].endswith(']$ ') or result['data'].endswith(']# '):
        ssh.close()
        return result['data']

