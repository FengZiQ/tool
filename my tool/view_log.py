# coding=utf-8
import paramiko
import time


def view_log(cmd):

    # 连接ssh
    ssh = paramiko.SSHClient()
    # 允许连接不在known_hosts文件上的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #
    ssh.connect(
        hostname='',
        username='',
        password=''
    )
    # 建立一个通道
    c = ssh.invoke_shell()

    # data接收通道返回数据的可变对象; timer：每个while最长运行5s后break
    result = {'data': '', 'timer': 0}

    # 发送go，打开跳板列表
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        time.sleep(1)
        result['timer'] += 1
        if result['data'].endswith(']$ ') or result['data'].endswith(']# ') or result['timer'] == 5:
            # print(result['data'])
            c.send(cmd + '\n')
            result['data'] = ''
            result['timer'] = 0
            break

    # 返回log内容
    while True:
        result['data'] += c.recv(9999).decode('utf-8')
        time.sleep(1)
        result['timer'] += 1
        if result['data'].endswith(']$ ') or result['data'].endswith(']# ') or result['timer'] == 5:
            # print(result['data'])
            break
    # print(result['timer'])
    ssh.close()
    return result['data']


if __name__ == "__main__":
    con = view_log('ls')
    print(con)
