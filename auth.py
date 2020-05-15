import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def clicker(driver, timeout, xpath):
    button = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((
            By.XPATH,
            xpath
        ))
    )
    button.click()


def main():

    link = 'https://toochka:toochka45@makecloud.online/'
    driver = webdriver.Chrome()
    driver.get(link)

    try:
        find_hamburger = driver.find_element_by_xpath('.//div[@class="shop hamburger"]')
        find_hamburger.click()

        # login_button = WebDriverWait(driver, 1).until(
        # EC.element_to_be_clickable((By.XPATH, './/span[contains(text(), "Вход")]')))
        # login_button.click()
        clicker(driver, 1, './/span[contains(text(), "Вход")]')

        # button = driver.find_element_by_xpath('.//button[@id="book"]')
        # button.click()

        # find_login_button = driver.find_element_by_xpath('.//span[contains(text(), "Вход")]')
        # find_login_button.click()

        # time.sleep(1)

        WebDriverWait(driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, './/iframe')))

        # driver.switch_to.frame(driver.find_element_by_xpath('.//iframe'))
        mail_input = driver.find_element_by_xpath('.//div/input[@name="login"]')
        mail_input.send_keys('admin')
        password_input = driver.find_element_by_xpath('.//div/input[@name="password"]')
        password_input.send_keys('1-qpwoei/')

        clicker(driver, 1, '//a[@class="link-button"][@id="submit"]')

        # submit_button = driver.find_element_by_xpath('//a[@class="link-button"][@id="submit"]')
        # time.sleep(1)
        # submit_button.click()
        print('TEST PASSED')

    finally:
        time.sleep(6)
        driver.quit()


if __name__ == '__main__':
    main()
