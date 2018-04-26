# -*- coding: utf-8 -*-
# 2018.04.05

import requests
import re
import xlrd
import json

data = xlrd.open_workbook('device.xlsx')
table = data.sheet_by_name('Sheet1')
device_no_list = [str(table.cell(i, 0).value) for i in range(1, table.nrows)]

provider_name = '测试账户'
excepted_version = '4.0.36'


def login():
    session = requests.session()
    # step1
    url1 = 'http://cas.2dupay.com/login?service=http%3A%2F%2Fdm.inspos.cn%2F'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://cas.2dupay.com/login?service=http%3A%2F%2Fdm.inspos.cn%2F',
        'Connection': 'keep-alive'
    }
    content1 = session.post(url1, headers=headers, verify=False)
    pattern1 = re.compile('.*?<input type="hidden" name="lt" value="(.*?)" />.*?')
    match1 = re.findall(pattern1, content1.text)
    ticket = match1[0]
    # step2
    url2 = 'http://cas.2dupay.com/login'
    cookies1 = content1.cookies.values()
    data = {
        'username': 'admin',
        'password': 'Inspiry2o17',
        'lt': ticket,
        'execution': 'e1s1',
        '_eventId': 'submit',
        'submit': 'LOGIN'
    }
    session.post(url2, data=data, json=None, headers=headers, cookies={'JSESSIONID': cookies1[0]}, verify=False)

    return session


def upgrade():
    session = login()
    flag = False

    result = session.post(
        'http://dm.inspos.cn/device/upgrade/edit',
        data=None,
        json={
            "deviceNoList": device_no_list,
            "upgradeInfoList": [{
                "name": "BasePayQBT_E",
                "version": ""
            }]
        }
    )

    text = json.loads(result.text)

    if text['code'] != 200:
        print('批量升级请求失败')
    else:
        print('批量升级请求成功')
        flag = True

    return flag


def check_result():
    session = login()

    customer_info = session.get(
        'http://dm.inspos.cn/customer/pageList?name=' + provider_name + '&salesName=&pageIndex=1&pageSize=15'
    )

    temp = json.loads(customer_info.text)

    customer_id = str(temp['data']['list'][0]['id'])

    for no in device_no_list:
        result = session.get(
            'http://dm.inspos.cn/deviceUpgrade/pageList?customerId=' +
            customer_id +
            '&pageIndex=1&pageSize=15&serialNum=' +
            no +
            '&connectState=0&operateType=sales'
        )

        temp1 = json.loads(result.text)

        try:
            app_name = json.loads(temp1['data']['list'][0]['appName'])
            actual_version = app_name['app']

            if actual_version == excepted_version:
                print('设备' + str(no) + '升级成功')
            else:
                print('设备' + str(no) + '升级失败')

        except KeyError:
            print('设备' + no + '升级失败')


if __name__ == "__main__":
    # upgrade()
    check_result()