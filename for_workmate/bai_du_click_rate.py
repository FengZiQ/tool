from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def bai_du_click_rate(key_words='', link_text=''):
    i = 0
    driver = webdriver.Firefox()
    # driver.maximize_window()
    driver.get('https://www.baidu.com/')
    first_page = driver.current_window_handle
    time.sleep(2)
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys(key_words)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    while i < 2000:

        driver.find_element_by_link_text(link_text).click()
        time.sleep(3)
        all_page = driver.window_handles

        for page in all_page:
            if page != first_page:
                driver.switch_to_window(page)

        driver.close()
        driver.switch_to_window(all_page[0])
        time.sleep(2)
        i += 1
        print(i)

if __name__ == "__main__":
    bai_du_click_rate(key_words='意锐小白盒', link_text='小白盒 – INSPIRY意锐')