import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# driver.get("https://www.baidu.com")
#
# driver.find_element()
# WebDriverWait(driver, 15, 1).until(EC.visibility_of_element_located)
# print(driver.title)

driver.get(r"file:///Users/chenxuanhuai/TESTDEV/Se2/myHTML.html")
# driver.get("file:///Users/chenxuanhuai/TESTDEV/Se2/myHTML.html")  # mac不加r也可以
driver.find_element(By.ID, "press").click()
alter = driver.switch_to.alert  # js的alert、confirm、prompt三个弹窗在 WebDriver中都是 alert处理
print(alter.text)
alter.accept()



time.sleep(1)
driver.quit()
