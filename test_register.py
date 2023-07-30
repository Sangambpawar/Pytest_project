import pytest


class Test_regi:
    @pytest.mark.skip  # pytest.mark.skip is used to skip the testcase here mark is small case
    def  test_reg(self):
        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import NoSuchElementException
        driver = webdriver.Chrome()

        # getting url
        driver.get('https://globalsqa.com/angularJs-protractor/registration-login-example/#/register')
        time.sleep(5)
        # click  on register
        # driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/form/div[3]/a').click()
        # time.sleep(5)

        # enter first name
        driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys('Sangam')
        # enter last name
        driver.find_element(By.XPATH, '//*[@id="Text1"]').send_keys('pawar')
        # enter username
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('Sangambpawar')
        # enter password
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sangam@123')
        time.sleep(5)
        # click on register
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div[5]/button').click()
        time.sleep(5)
        # enter username
        driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('Sangambpawar')
        # enter pass
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sangam@123')
        time.sleep(5)
        # click on login
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/form/div[3]/button').click()
        time.sleep(10)
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/h1')
            print('test is pass')
            assert True
        except NoSuchElementException:
            print('test is pass')
            assert False
