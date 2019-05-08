# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from to_log import testlink, all_logs
from configFile import login_data
from reuseBrowser import ReuseFirefox


class GUITestTool(object):
    # 初始化
    def __init__(self):
        # 标记用例执行结果
        self.Pass = "'result': 'p'"
        self.Fail = "'result': 'f'"
        # 标记用例执行状态
        self.FailedFlag = False
        # 打开火狐浏览器，实现重用
        self.oldD = webdriver.Firefox()
        self.oldD.maximize_window()
        executor_url = self.oldD.command_executor
        session_id = self.oldD.session_id
        self.oldD.get(login_data['url'])
        # del self.oldD
        self.driver = ReuseFirefox(command_executor=executor_url, session_id=session_id)

    def login(self):
        pass

    """
    locator type: 
    By.ID, # By.ID时有bug
    By.NAME,
    By.CLASS_NAME,
    By.TAG_NAME,
    By.LINK_TEXT,
    By.PARTIAL_LINK_TEXT,
    By.XPATH,
    By.CSS_SELECTOR
    """
    # 鼠标左键
    def click_action(self, path, location, locator=By.XPATH, response_time=3):
        try:
            self.driver.find_element(locator, path).click()
            time.sleep(response_time)
        except Exception as e:
            print(e)
            self.FailedFlag = True
            all_logs(location + ' is not found')
            testlink(location + ' is not found')

    # 填写文本框
    def fill_action(self, path, value, location, locator=By.XPATH, response_time=1):

        try:
            self.driver.find_element(locator, path).clear()
            self.driver.find_element(locator, path).send_keys(value)
            time.sleep(response_time)
        except Exception as e:
            print(e)
            self.FailedFlag = True
            all_logs(location + ' is not found')
            testlink(location + ' is not found')

    # 等待元素出现并获取其的文本
    def wait_for_element(self, path, location, locator=By.XPATH):
        text = ''
        for i in range(30):
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

    # 断言特定值与元素的文本相等；每条case的最后一个断言end = '@结束@'
    def equal_text_assert(self, path, location, expected_text, end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + ': ' + expected_text)
            actual_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + ': ' + actual_text)
            testlink(location + ': ' + actual_text)
            testlink(end)
            if actual_text != expected_text:
                self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 断言某些文本出现在元素的文本中；每条case的最后一个断言end = '@结束@'
    def contained_text_assert(self, path, location, expected_text=list(), end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + '包括: ' + str(expected_text))
            actual_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + ': \n' + actual_text)
            testlink(location + ': ' + actual_text)
            testlink(end)
            for t in expected_text:
                if t not in actual_text:
                    self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 断言某些文本没有出现在元素的文本中；每条case的最后一个断言end = '@结束@'
    def no_text_assert(self, path, location, expected_text=list(), end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + '中不包括' + str(expected_text))
            page_text = self.driver.find_element(locator, path).text
            all_logs('实际结果: ' + location + '中内容为”\n' + page_text + '"')
            testlink(location + '中内容为”\n' + page_text + '"')
            testlink(end)
            for t in expected_text:
                if t in page_text:
                    self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 断言某个元素不存在；每条case的最后一个断言end = '@结束@'
    def element_not_exist_assert(self, path, location, end='', locator=By.XPATH):
        try:
            all_logs('期望结果: ' + location + '不存在')
            self.driver.find_element(locator, path)
        except:
            all_logs('实际结果: ' + location + '不存在')
            testlink(location + '不存在')
            testlink(end)
        else:
            self.FailedFlag = True
            all_logs('实际结果: ' + location + ' 存在')
            testlink(location + ' 存在')
            testlink(end)

    # 断言操作是否触发了log生成；每条case的最后一个断言end = '@结束@'
    def log_assert(self, log_text='', expected_text=list(), end=''):
        all_logs('期望结果：操作触发生成的log中包括' + str(expected_text))
        for text in expected_text:
            if text not in log_text:
                self.FailedFlag = True
        all_logs('实际结果：操作触发生成的log:\n' + log_text.replace('[01;31m[K', '').replace('[m[K', ''))
        testlink('操作触发生成的log:\n' + log_text.replace('[01;31m[K', '').replace('[m[K', ''))
        testlink(end)

    # 断言元素的属性
    def element_attribute(self, path, location, attr_name, expected, end='', locator=By.XPATH):
        try:
            attr = self.driver.find_element(locator, path).get_attribute(attr_name)
            all_logs('期望结果：' + location + '的' + attr_name + '属性值为' + expected)
            all_logs('实际结果：' + location + '的' + attr_name + '属性值为' + attr)
            testlink(location + '的' + attr_name + '属性值为' + attr)
            testlink(end)
            if attr != expected:
                self.FailedFlag = True
        except Exception as e:
            self.FailedFlag = True
            all_logs('实际结果: ' + str(e))
            testlink(str(e))
            testlink(end)
            all_logs(location + ' is not found\n')

    # 标记case执行通过状态
    def mark_status(self):
        if self.FailedFlag:
            all_logs('-*- The case is executed -*-\n')
            all_logs(self.Fail)
            testlink(self.Fail + '\n')
            self.FailedFlag = False
        else:
            all_logs('-*- The case is executed -*-\n')
            all_logs(self.Pass)
            testlink(self.Pass + '\n')

    def finished(self):
        self.driver.quit()


tool = GUITestTool()
