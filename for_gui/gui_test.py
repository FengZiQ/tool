# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from to_log import *
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
        # IE 浏览器测试
        # self.driver = webdriver.Ie()
        # 谷歌浏览器测试
        # self.driver = webdriver.Chrome()
        # 火狐狸浏览器测试
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(base_url)
        self.driver.find_element_by_id('username').send_keys(self.user)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element_by_id('captcha').send_keys('123456')
        self.driver.find_element_by_id("loginSubmit").click()
        time.sleep(3)

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
            all_logs(location + ' is not found')

    def fill_action(self, path, value, location, locator=By.XPATH, response_time=1):

        try:
            self.driver.find_element(locator, path).clear()
            self.driver.find_element(locator, path).send_keys(value)
            time.sleep(response_time)
        except Exception as e:
            print(e)
            all_logs(location + ' is not found')

    # 每条case的最后一个断言end = '@结束@'
    def equal_text_assert(self, path, location, expected_text, end='', locator=By.XPATH):
        all_logs('期望结果: ' + location + ': ' + expected_text)
        try:
            actual_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + ': ' + actual_text)
            testlink(location + ': ' + actual_text)
            testlink(end)
            if actual_text != expected_text:
                self.FailFlag = True
        except Exception as e:
            self.FailFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 每条case的最后一个断言end = '@结束@'
    def contained_text_assert(self, path, location, expected_text, end='', locator=By.XPATH):
        all_logs('期望结果: ' + location + ': ' + expected_text)
        try:
            actual_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + ': ' + actual_text)
            testlink(location + ': ' + actual_text)
            testlink(end)
            if expected_text in actual_text:
                self.FailFlag = True
        except Exception as e:
            self.FailFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    def wait_for_element(self, path, location, locator=By.XPATH):
        text = ''
        for i in range(10):
            try:
                if self.driver.find_element(locator, path):
                    text += self.driver.find_element(locator, path).text
                    break
            except Exception as e:
                print(e)
                all_logs(location + ' is not found\n')
                break
            time.sleep(1)
        else:
            all_logs('time out')

        return text

    def finished(self):
        self.driver.close()

    def mark_status(self):

        if self.FailFlag:
            all_logs('-*- The case is executed -*-\n')
            all_logs(Fail)
            testlink(Fail + '\n')
        else:
            all_logs('-*- The case is executed -*-\n')
            all_logs(Pass)
            testlink(Pass + '\n')


tool = GUITestTool()
