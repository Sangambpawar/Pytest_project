# import time
#
# import pytest
#
#
# class Test_bank:
#     @pytest.mark.credence
#
#
#
#     def test_validate_url(self):
#         import time
#
#         from selenium import webdriver
#         from selenium.webdriver.common.alert import Alert
#         from selenium.webdriver.common.by import By
#         from selenium.common import NoSuchElementException
#         from selenium.webdriver.support.select import Select
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(20)
#         driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
#         try:
#             driver.find_element(By.XPATH,'/html/body/div/div/div[1]/strong')
#             print('url test case is pass')
#             assert True
#         except NoSuchElementException:
#             print('url test case is  fail')
#             assert False
#
#     @pytest.mark.credence
#     def test_home(self):
#         from selenium import webdriver
#         from selenium.webdriver.common.alert import Alert
#         from selenium.webdriver.common.by import By
#         from selenium.common import NoSuchElementException
#         from selenium.webdriver.support.select import Select
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(10)
#         driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
#         #  1)click on custmer loggin
#         driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/div[1]/button').click()
#         # select your name
#         a = Select(driver.find_element(By.XPATH, '//*[@id="userSelect"]'))
#         a.select_by_index(2)
#         #  click on loggin button
#         driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/button').click()
#         time.sleep(2)
#         b = Select(driver.find_element(By.XPATH, '//*[@id="accountSelect"]'))
#         b.select_by_index(1)
#         # click on transection
#         driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[3]/button[1]').click()
#         # select transection
#         print('this is system genrated statment :',
#               driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[2]/table/thead/tr').text)
#         # validate back button
#         driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/div[1]/button[1]').click()
#         # click  on home button validate
#         driver.find_element(By.XPATH, '/html/body/div/div/div[1]/button[1]').click()
#         try:
#             driver.find_element(By.XPATH, '/html/body/div/div/div[1]/strong')
#             print('customer login is  pass')
#             assert True
#         except NoSuchElementException:
#             print('customer login test is failed')
#             assert False
