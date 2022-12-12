from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from PIL import ImageDraw
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(executable_path=r'D:/etc/chromedriver.exe', chrome_options=options)
driver.get('https://github.com/tealle314/djy/blob/master/gb/22/1/10/n13494094.md#1')
driver.implicitly_wait(3)
# 找到第一个主题所在位置
target = driver.find_element(by=By.XPATH, value='//*[@id="readme"]/article/table/tbody/tr[3]/td[1]/p[1]')
# target.send_keys(Keys.DOWN)
location = target.location
tagetSize = target.size
x = location['x']
y = location['y']
# 页面滚动到第一个主题所在位置
driver.execute_script("window.scrollTo(0, " + str(y) + ")")
# 截取当前网页页面
driver.save_screenshot("pageImage.png")
# 根据已经知道的位置， 和主题的大小， 给截图页面画上红框框
redLine = Image.open("pageImage.png")
redDraw = ImageDraw.ImageDraw(redLine)
redDraw.rectangle(((5,5),(tagetSize['width'], tagetSize['height'])), fill=None, outline='red', width=5)
redLine.save("pageImageWithRedLine.png")
# 找到第二个主题的位置
target2 = driver.find_element(by=By.XPATH, value='//*[@id="readme"]/article/table/tbody/tr[3]/td[1]/h2[2]')
location2 = target2.location
x2 = location2['x']
y2 = location2['y']
width = target.size['width']
height = y2 - y
im = Image.open('pageImageWithRedLine.png')
# 根据第一个主题和第二个主题的位置差， 截取当中内容
im = im.crop((0, 0, int(width), int(height)))
im.save('element.png')
driver.quit()
