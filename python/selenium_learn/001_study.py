from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
def test_python_web():
    # 基础操作1：打开一个会话
    driver = webdriver.Chrome(r'D:\etc\Drivers\chromedriver.exe')
    # drvier = webdriver.Firefox(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    # 基础操作2：操作浏览器 - 打开一个网页
    driver.get('http://www.python.org')
    # driver.title 基础操作3：从浏览器上获取一些信息
    assert 'Python' in driver.title
    # 基础操作4：主动创建等待策略
    driver.implicitly_wait(0.5)
    # 基础操作5：搜索组件
    elem = driver.find_elements(by=By.NAME, value="q")
    search_box = elem[0]
    # 基础操作6： 操作这个组件
    search_box.clear()
    search_box.send_keys('pycon')
    search_box.send_keys(Keys.RETURN)
    assert 'No results found.' not in driver.page_source
    # 基础操作8： 结束这个会话
    # driver.close()
def test_eight_components():
    driver = webdriver.Chrome(r'D:\etc\Drivers\chromedriver.exe')
    driver.get("https://google.com")
    title = driver.title
    assert title == "Google"
    driver.implicitly_wait(0.5)
    search_box = driver.find_elements(by=By.NAME, value="q")[0]
    search_button = driver.find_elements(by=By.NAME, value="btnK")[0]
    search_box.send_keys("Selenium")
    search_button.click()
    search_box = driver.find_elements(by=By.NAME, value="q")[0]
    value = search_box.get_attribute("value")[0]
    assert value == "Selenium"
    # driver.quit()
if __name__ == '__main__':
    test_eight_components()
