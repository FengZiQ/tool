from selenium import webdriver


def d():
    driver0 = webdriver.Firefox()
    executor_url = driver0.command_executor._url
    session_id = driver0.session_id
    print(session_id)
    print(executor_url)

    driver1 = webdriver.Remote(command_executor=executor_url, desired_capabilities={}, keep_alive=True)
    driver1.session_id = session_id
    return driver1


driver = d()
