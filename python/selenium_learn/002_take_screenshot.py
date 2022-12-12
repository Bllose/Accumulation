from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
def example_one():
    driver = webdriver.Chrome(r'D:/etc/chromedriver.exe')
    driver.get("https://python.org")
    driver.save_screenshot("screenshot.png")
    driver.close()
def example_two():
    # take screenshot
    driver = webdriver.Chrome(r'D:/etc/chromedriver.exe');
    driver.get('https://www.baidu.com/');
    element = driver.find_element(by=By.ID, value="s_lg_img");
    location = element.location;
    size = element.size;
    driver.save_screenshot("pageImage.png");
    # crop image
    x = location['x'];
    y = location['y'];
    width = location['x']+size['width'];
    height = location['y']+size['height'];
    im = Image.open('pageImage.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save('element.png')
    driver.quit()
if __name__ == '__main__':
    example_two()
