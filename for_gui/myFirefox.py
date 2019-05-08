# coding=utf-8
from selenium import webdriver


driver = webdriver.Chrome()
url = driver.command_executor._url
session_id = driver.session_id
driver2 = webdriver.Remote(command_executor=url, desired_capabilities={})

