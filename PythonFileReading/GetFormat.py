from bs4 import BeautifulSoup
from selenium import webdriver



driver = webdriver.Chrome('C:/Users/Ariel/Downloads/chromedriver_win32/chromedriver')
driver.implicitly_wait(3)

driver.get('http://1.231.29.235/Account/LogOn')

driver.find_element_by_name('UserName').send_keys('khy4701')
driver.find_element_by_name('Password').send_keys('ghdud159753')

element = driver.find_element_by_xpath("//a[contains(@href,'fnSubmit')]")
element.click()

driver.implicitly_wait(3)

driver.get('http://1.231.29.235/Ea/EADocPop/EAAppDocPop/?form_id=31')

driver.implicitly_wait(5)
element = driver.find_element_by_xpath("//span[@id='cke_32_label']")
element.click()

driver.implicitly_wait(3)

element = driver.find_element_by_xpath("//*[@id='cke_1_contents']/textarea")
print (element.get_attribute("value"))

f = open("D:/Users/Ariel/workspace/PythonFileReading/parsing.txt", 'w')
f.write(element.get_attribute("value"))
f.close()


