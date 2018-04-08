# -*- coding: utf-8 -*-
# 2018.04.05

import requests
import re
import time
import os
from selenium import webdriver


def login_step1():
    j_session_id = 'DC7AA682E6559879EB5F5E105DCD2AC2'
    url = 'http://cas.2dupay.com/login?;jsessionid=' + j_session_id + 'service=http%3A%2F%2Fdm.inspos.cn%2F'

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Content-Length': '139',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'JSESSIONID=' + j_session_id,
        'Host': 'cas.2dupay.com',
        'Referer': 'http://cas.2dupay.com/login?service=http%3A%2F%2Fdm.inspos.cn%2F',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }
    login_para = {
        'username': 'inspos',
        'password': 'inspos',
        'lt': 'LT-805679-AhB21Mf3WLKxl3m1GsrlXDedFUigBK-2dupay',
        'execution': 'e1s1',
        '_eventId': 'submit',
        'submit': '登录'
    }
    session = requests.session()
    content = session.post(url, headers=headers, data=login_para)
    pattern = re.compile('.*?<input type="hidden" name="lt" value="(.*?)" />.*?')
    match = re.findall(pattern, content.text)
    lt = match[0]
    print(lt)
    return lt


def login_step2():
    url = 'http://dm.inspos.cn/'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'Host': 'dm.inspos.cn',
        'Referer': 'http://cas.2dupay.com/login?service=http%3A%2F%2Fdm.inspos.cn%2F',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'
    }
    ticket = login_step1()
    session = requests.session()
    content = session.get(url + '?ticket=' + ticket, headers=headers)

    print(content.text.encode('utf-8'))


def get_text():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F')
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id("password").send_keys('123321qwe')
    driver.find_element_by_id("loginSubmit").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="seriveDropdownMenu"]').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/span[1]/div/ul/li[4]/a').click()

    temp1_link = [link.get_attribute("href") for link in driver.find_elements_by_tag_name("a") if link]

    temp2_link = [temp3_link for temp3_link in temp1_link if temp3_link not in [None, 'index.htmljavascript:void(0);', 'javascript:void(0);']]
    page_link = str(set([temp4_link for temp4_link in temp2_link if '#' in temp4_link])).replace('{', '').replace('}', '').split(',')

    for link in page_link:
        print(link.replace("'", ''))
        driver.get(link.replace("'", ''))
        time.sleep(10)
        temp1_text = driver.find_element_by_tag_name('body').text
        temp2_text = [re.sub("[A-Za-z0-9\!\%\[\]\,\。\：]", "", text) for text in temp1_text.split('\n')]
        page_text = [temp3_text for temp3_text in temp2_text if temp3_text not in ['', '_']]

        with open("page_text.txt", "r+", encoding='UTF-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(link + '\n' + str(set(page_text)) + '\n\n\n' + content)

        print(set(page_text))

    driver.close()

if __name__ == "__main__":
    get_text()