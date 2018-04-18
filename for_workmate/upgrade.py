# -*- coding: utf-8 -*-
# 2018.04.05

import requests
import re


def login():
    session = requests.session()

    # step1
    url1 = 'http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F',
        'Connection': 'keep-alive'
    }
    content1 = session.post(url1, headers=headers)
    # print(content1.text)
    pattern1 = re.compile('.*?<input type="hidden" name="lt" value="(.*?)" />.*?')
    match1 = re.findall(pattern1, content1.text)
    ticket = match1[0]

    # step2
    url2 = 'http://cas.testing.2dupay.com/login?'
    cookies1 = content1.cookies.values()
    data = {
        'username': 'admin',
        'password': '123321qwe',
        'lt': ticket,
        'execution': 'e1s1',
        '_eventId': 'submit',
        'submit': 'LOGIN'
    }
    for k, v in data.items():
        url2 += k + '=' + v + '&'
    content2 = session.post(url2[:-1], headers=headers, cookies={'JSESSIONID': cookies1[0]})
    # print(content2.text)

    # step3
    cookies2 = content2.history[1].cookies.values()
    content3 = session.get(
        'http://dm.testing.inspos.cn/homeIndex.html',
        cookies={'JSESSIONID': cookies2[0]},
        verify=False
    )
    print(content3.text)

    get_url_result = session.get('http://dm.testing.inspos.cn/index.html#equipmentShow')

    result = session.post(
        'http://dm.testing.inspos.cn/device/upgrade/edit',
        headers={
            'Content-Type': 'application/json',
            'Referer': 'http://dm.testing.inspos.cn/index.html',
            'Host': 'dm.testing.inspos.cn',
            'Connection': 'keep-alive'
        },
        data={"deviceNoList": ["3333333333222222222"], "upgradeInfoList": [{"name": "BasePayQBT_E", "version": ""}]},
        cookies={'JSESSIONID': cookies2[0]}
    )

    print('ha')


if __name__ == "__main__":
    login()