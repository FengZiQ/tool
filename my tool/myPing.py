# coding=utf8
import subprocess
import re


# 获取链路状态
def get_link_state(ip):
    ping_data = {}
    # 运行ping程序
    p = subprocess.Popen(
        ["ping.exe", ip],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )

    # 得到ping的结果
    out = p.stdout.read().decode('utf-8', 'ignore')
    print(out)
    # 找出丢包率，通过‘%’匹配
    regex = re.compile(r'\w*%\w*')
    loss_rate = regex.findall(out)

    # 找出往返时间，通过‘ms’匹配
    regex = re.compile(r'\w*ms')
    time_list = regex.findall(out)
    try:
        ping_data['lossRate'] = loss_rate[0]
        ping_data['minTime'] = time_list[-3]
        ping_data['maxTime'] = time_list[-2]
        ping_data['averageTime'] = time_list[-1]

        return ping_data
    except IndexError:
        print('地址:' + ip + ' ping不通')
        return None


if __name__ == "__main__":
    print(get_link_state('192.168.233.68'))
