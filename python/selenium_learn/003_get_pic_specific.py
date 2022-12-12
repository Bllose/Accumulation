from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(executable_path=r'D:/etc/chromedriver.exe', chrome_options=options)
driver.get('https://github.com/tealle314/djy/blob/master/gb/22/1/10/n13494094.md#1')
driver.implicitly_wait(3)
target = driver.find_element(by=By.XPATH, value='//*[@id="readme"]/article/table/tbody/tr[3]/td[1]/p[1]')
# target.send_keys(Keys.DOWN)
location = target.location
y = location['y']
driver.execute_script("window.scrollTo(0, " + str(y) + ")")
driver.implicitly_wait(3)
print('DONE!')
