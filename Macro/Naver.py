from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Ariel/Downloads/chromedriver_win32/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys('ghdud4701')
driver.find_element_by_name('pw').send_keys('hoyoung159753')

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
