from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.XPATH,'//*[@id="num1"]')
    num2 = browser.find_element(By.XPATH,'//*[@id="num2"]')
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    print(int(num1.text) + int(num2.text))
    select.select_by_value(str(int(num1.text) + int(num2.text)))

    browser.find_element(By.XPATH, '//div//form//button').click()

finally:
	# waiting 30 secs
    time.sleep(30)
    browser.quit()
