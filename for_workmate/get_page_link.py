# -*- coding: utf-8 -*-
# 2018.04.05

import time
from selenium import webdriver


def get_testing_platform_all_link():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F')
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id("password").send_keys('123321qwe')
    driver.find_element_by_id("loginSubmit").click()
    time.sleep(5)

    data = {
        # 'bi': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[1]/a', 'BI数据统计平台'],
        'dm': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[2]/a', '设备管理平台'],
        'sp': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[4]/a', '商户管理平台'],
        'bus': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[5]/a', '公交管理平台'],
        'app': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[6]/a', 'app后台管理平台'],
        'open': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[7]/a', '开放支付平台'],
        'perm': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[8]/a', '权限管理平台'],
        'mss': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[3]/a', '生产管理平台']
    }

    for key in list(data.keys()):

        driver.find_element_by_xpath(data[key][0]).click()
        time.sleep(1)
        driver.find_element_by_xpath(data[key][1]).click()
        time.sleep(5)

        temp1_link = [link.get_attribute("href") for link in driver.find_elements_by_tag_name("a") if link]

        temp2_link = [temp3_link for temp3_link in temp1_link if temp3_link not in [None, 'index.htmljavascript:void(0);', 'javascript:void(0);']]
        page_link = str(set([temp4_link for temp4_link in temp2_link if '#' in temp4_link])).replace('{', '').replace('}', '').replace(',', ',\n')

        with open("testing_all_link.txt", "r+", encoding='UTF-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('\n\n' + data[key][2] + '\n' + page_link + content)
            f.close()


def get_preo_platform_all_link():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://cas.preo.2dupay.com/login?service=http%3A%2F%2Fdm.preo.inspos.cn%2F')
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id("password").send_keys('123321qwe')
    driver.find_element_by_id("loginSubmit").click()
    time.sleep(5)

    data = {
        'bi': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[1]/a', 'BI数据统计平台'],
        'dm': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[2]/a', '设备管理平台'],
        'sp': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[4]/a', '商户管理平台'],
        'bus': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[5]/a', '公交管理平台'],
        'app': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[6]/a', 'app后台管理平台'],
        'open': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[7]/a', '开放支付平台'],
        'perm': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[8]/a', '权限管理平台'],
        'mss': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[3]/a', '生产管理平台']
    }

    for key in list(data.keys()):

        driver.find_element_by_xpath(data[key][0]).click()
        time.sleep(1)
        driver.find_element_by_xpath(data[key][1]).click()
        time.sleep(5)

        temp1_link = [link.get_attribute("href") for link in driver.find_elements_by_tag_name("a") if link]

        temp2_link = [temp3_link for temp3_link in temp1_link if temp3_link not in [None, 'index.htmljavascript:void(0);', 'javascript:void(0);']]
        page_link = str(set([temp4_link for temp4_link in temp2_link if '#' in temp4_link])).replace('{', '').replace('}', '').replace(',', ',\n')

        with open("preo_all_link.txt", "r+", encoding='UTF-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('\n\n' + data[key][2] + '\n' + page_link + content)
            f.close()


def get_official_platform_all_link():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://cas.2dupay.com/login?service=http%3A%2F%2Fdm.inspos.cn%2F')
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id("password").send_keys('Inspiry2o17')
    driver.find_element_by_id("loginSubmit").click()
    time.sleep(5)

    data = {
        'bi': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[1]/a', 'BI数据统计平台'],
        'dm': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[2]/a', '设备管理平台'],
        'sp': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[4]/a', '商户管理平台'],
        'bus': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[5]/a', '公交管理平台'],
        'app': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[6]/a', 'app后台管理平台'],
        'open': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[7]/a', '开放支付平台'],
        'perm': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[8]/a', '权限管理平台'],
        'mss': ['//*[@id="seriveDropdownMenu"]', '/html/body/div[2]/div[1]/span[1]/div/ul/li[3]/a', '生产管理平台']
    }

    for key in list(data.keys()):

        driver.find_element_by_xpath(data[key][0]).click()
        time.sleep(1)
        driver.find_element_by_xpath(data[key][1]).click()
        time.sleep(5)

        temp1_link = [link.get_attribute("href") for link in driver.find_elements_by_tag_name("a") if link]

        temp2_link = [temp3_link for temp3_link in temp1_link if temp3_link not in [None, 'index.htmljavascript:void(0);', 'javascript:void(0);']]
        page_link = str(set([temp4_link for temp4_link in temp2_link if '#' in temp4_link])).replace('{', '').replace('}', '').replace(',', ',\n')

        with open("official_all_link.txt", "r+", encoding='UTF-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('\n\n' + data[key][2] + '\n' + page_link + content)
            f.close()


if __name__ == "__main__":
    # get_testing_platform_all_link()
    # get_preo_platform_all_link()
    get_official_platform_all_link()