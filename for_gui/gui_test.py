# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from to_log import tolog
import time

Pass = "'result': 'p'"
Fail = "'result': 'f'"


class GUITestTool(object):

    server = "http://cas.testing.2dupay.com/login?service=http%3A%2F%2Fdm.testing.inspos.cn%2F"

    def __init__(self, base_url=server):
        # login user and username
        self.user = 'admin'
        self.password = '123321qwe'

        # mark test cases execution status
        self.FailFlag = False

        # execution login
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.driver.find_element_by_id('username').send_keys(self.user)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id("loginSubmit").click()
        time.sleep(3)

    def finished(self):
        self.driver.close()

    """
    locator type: 
    By.ID,By.NAME,By.CLASS_NAME,By.TAG_NAME,By.LINK_TEXT,By.PARTIAL_LINK_TEXT,By.XPATH,By.CSS_SELECTOR
    """
    def click_action(self, path, location, locator=By.XPATH, response_time=3):

        try:
            self.driver.find_element(locator, path).click()
            time.sleep(response_time)
        except Exception as e:
            print(e)
            tolog(location + ' is not found\n')

    def fill_action(self, path, value, location, locator=By.XPATH, response_time=1):

        try:
            self.driver.find_element(locator, path).clear()
            self.driver.find_element(locator, path).send_keys(value)
            time.sleep(response_time)
        except Exception as e:
            print(e)
            tolog(location + ' is not found\n')

    def element_text_assert(self, path, location, expected_text, actual_text='', locator=By.XPATH):

        try:
            actual_text = actual_text + self.driver.find_element(locator, path).text
            if actual_text != expected_text:
                self.FailFlag = True
                tolog(actual_text + '\n')
                tolog('-*- The case is executed -*-\n')
            else:
                tolog(actual_text + '\n')
                tolog('-*- The case is executed -*-\n')
        except Exception as e:
            print(e)
            tolog(location + ' is not found\n')
            tolog('-*- The case is executed -*-' + '\n')

    def page_text_assert(self, expected_text):
        result = self.driver.find_element_by_tag_name('body').text

        if expected_text not in result:
            self.FailFlag = True
            tolog('页面中没有 ' + expected_text + '\n')
            tolog('-*- The case is executed -*-\n')
        else:
            tolog('页面中有 ' + expected_text + '\n')
            tolog('-*- The case is executed -*-\n')

    def wait_for_element(self, path, location, locator=By.XPATH):

        for i in range(10):
            try:
                if self.driver.find_element(locator, path):
                    break
            except Exception as e:
                print(e)
                tolog(location + ' is not found\n')
                break
            time.sleep(1)
        else:
            tolog('time out')

        return

    def mark_status(self):

        if self.FailFlag:
            tolog(Fail)
        else:
            tolog(Pass)