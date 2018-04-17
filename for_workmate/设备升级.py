# -*- coding: utf-8 -*-
# 2018.04.12

from selenium import webdriver
from selenium.webdriver.common.by import By
import xlrd
import time


def update():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F')
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id("password").send_keys('123321qwe')
    driver.find_element_by_id("loginSubmit").click()
    time.sleep(3)
    # 设备管理
    driver.find_element(By.XPATH, '//*[@id="leftNav"]/li[3]/a').click()
    # 已销售设备
    driver.find_element(By.XPATH, '//*[@id="leftNav"]/li[3]/ul/li[3]/a').click()
    time.sleep(5)
    # 服务商名称框
    driver.find_element(By.XPATH, '//*[@id="checkBoundDeviceContainer"]/div[1]/div/button').click()
    # 服务商名称
    driver.find_element(By.XPATH, '//*[@id="checkBoundDeviceContainer"]/div[1]/div/div/ul/li[213]/a/span[1]').click()

    # 数据
    data = xlrd.open_workbook('device.xlsx')
    table = data.sheet_by_name('Sheet1')

    for i in range(1, table.nrows):

        device_no = table.cell(i, 0).value
        excepted_release = ''

        # 输入设备号
        driver.find_element(By.XPATH, '//*[@id="queryDeviceId"]').send_keys(device_no)
        # 查询
        driver.find_element(By.XPATH, '//*[@id="checkBoundDeviceContainer"]/div[1]/button').click()
        time.sleep(3)
        # 点击复选框选择设备
        driver.find_element(By.XPATH, '//*[@id="devicesTbody"]/tr/td[1]/div/ins').click()
        # 点击设备升级按钮
        driver.find_element(By.XPATH, '//*[@id="addbtn"]').click()
        # 选择所需软件
        driver.find_element(By.XPATH, '//*[@id="ppbutler"]').submit()
        # 选择所需版本
        driver.find_element(By.XPATH, '//*[@id="ppbutler"]/option[17]').click()
        # 点击确认升级按钮
        driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[6]/div/div/div[3]/button[1]').click()

        actual_release = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[12]').text

        if actual_release != excepted_release:
            print(actual_release)

if __name__ == "__main__":
    update()