import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.supremenewyork.com/shop/shoes/w8fsl0j1g/b0y4ecjmk')

html = driver.page_source
sold_out = driver.find_element(by=By.ID, value='cctrl')
sold_out_button = sold_out.find_element(by=By.CLASS_NAME, value='button.sold-out')

if sold_out_button:
    print(type(sold_out_button))
    print(sold_out_button.text)
else:
    print('not sold out')

