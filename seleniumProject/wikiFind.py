import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")

search_box = driver.find_element(By.ID, "searchInput")
time.sleep(2)
search_box.send_keys("Python")
search_box.submit()
time.sleep(2)

web_link = driver.find_element(By.LINK_TEXT, "Python (mythology)")
web_link.click()
time.sleep(2)
driver.quit()