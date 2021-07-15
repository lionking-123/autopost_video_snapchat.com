import os
import sys
import time
import glob
from pywinauto import Desktop

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = webdriver.chrome.service.Service(os.path.abspath('chromedriver'))
service.start()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(os.path.abspath('chromedriver'), options=option)
url = 'https://my.snapchat.com/'
driver.get(url)
time.sleep(3)

btn = driver.find_element_by_css_selector('button.ant-btn')
btn.click()
time.sleep(0.5)

usr = driver.find_element_by_css_selector("input[name='username']")
usr.send_keys("agnesa.muqa")
pwd = driver.find_element_by_css_selector("input[name='password']")
pwd.send_keys("anagashi112")

btn = driver.find_element_by_css_selector("button[type='submit']")
btn.click()
time.sleep(1)

btn = driver.find_element_by_css_selector("button[type='submit']")
btn.click()

try:
    vidBtn = WebDriverWait(driver, 160).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.primary')))
except:
    driver.quit()

filePath = "C:\\Users\\Administrator\\Documents\\vroom"
vFiles = glob.glob(filePath + "\\*.mp4")
print(len(vFiles))


for fn in vFiles:
    try:
        trash = driver.find_element_by_css_selector("i.icon-trash")
        trash.click()
        time.sleep(1)
    except:
        pass

    vidBtn = driver.find_elements_by_css_selector("button.primary")[0]
    vidBtn.click()

    app = Desktop().window(title="Open")
    app.type_keys(fn)
    app.type_keys("{ENTER}")
    time.sleep(5)

    try:
        vid = driver.find_element_by_css_selector("i.icon-trash")

        try:
            acceptBtn = driver.find_element_by_css_selector("button.elevated")
            acceptBtn.click()
            time.sleep(0.5)

            okBtn = driver.find_element_by_css_selector(
                "div.ant-modal-footer > div > button.primary")
            okBtn.click()
        except:
            pass

        sbBtn = driver.find_elements_by_css_selector("button.primary")[0]
        sbBtn.click()

        time.sleep(120)
        newBtn = driver.find_element_by_css_selector("button.elevated")
        newBtn.click()

    except:
        pass
