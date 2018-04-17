# -*- coding: utf-8 -*-
# 2018.04.05

import re
import time
import os
from selenium import webdriver


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


def get_files_name():
    all_files_name = []
    for (dirPath, dirs, all_files_name) in os.walk(r'D:\script\tool\for_workmate\DM_html'):
        pass
    return all_files_name


def html_get_text():
    names = get_files_name()
    temp_text = []
    for file in names:
        open_file = open('DM_html/' + file, 'r', encoding='utf-8')
        content = open_file.read()

        temp = re.sub('[A-Za-z0-9\!\%\[\]\,\。\：\<\>\=\-\/\(\)\:\;\_\*\#\&\×\！\+\$\?\@\\"]', '', content)
        temp1 = [line.strip() for line in temp.split('\n')]
        temp_text += temp1

        open_file.close()

    with open("page_text.txt", "r+", encoding='UTF-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(str(set(temp_text)).replace(',', '\n').replace('{', '').replace('}', '').replace('.', '') + '\n\n' + content)
        f.close()


if __name__ == "__main__":
    # get_text()
    html_get_text()