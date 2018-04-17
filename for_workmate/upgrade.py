# -*- coding: utf-8 -*-
# 2018.04.05

import requests
import re


def login():
    session = requests.session()

    # step1
    url0 = 'http://cas.testing.2dupay.com/login?service=http://dm.testing.inspos.cn/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Referer': 'http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F',
        'Connection': 'keep-alive'
    }

    content0 = session.post(url0, headers=headers, verify=False)
    # print(content0.text)

    pattern0 = re.compile('.*?<input type="hidden" name="lt" value="(.*?)" />.*?')
    match0 = re.findall(pattern0, content0.text)
    ticket = match0[0]

    # step2
    url1 = 'http://cas.testing.2dupay.com/login?'

    data = {
        'username': 'admin',
        'password': '123321qwe',
        'lt': ticket,
        'execution': 'e1s1',
        '_eventId': 'submit',
        'submit': 'LOGIN'
    }

    for k, v in data.items():
        url1 += k + '=' + v + '&'

    session.post(url1[:-1], headers=headers, verify=False)

    result = session.post(
        'http://dm.testing.inspos.cn/device/upgrade/edit',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://dm.testing.inspos.cn/index.html',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Host': 'dm.testing.inspos.cn'
        },
        data={"deviceNoList": ["3333333333222222222"], "upgradeInfoList": [{"name": "BasePayQBT_E", "version": ""}]},
        verify=False
    )

    print('ha')


if __name__ == "__main__":
    login()