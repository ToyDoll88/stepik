import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

try:
    # browser = webdriver.Chrome()
    # browser.get('http://suninjuly.github.io/explicit_wait2.html')

    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, './/h5[@id="price"]'),
                                         '$100'))
    button = browser.find_element_by_xpath('.//button[@id="book"]')
    button.click()

    x = browser.find_element_by_xpath('.//span[@id="input_value"]').text
    y = calc(x)

    answer = browser.find_element_by_xpath('.//input[@id="answer"]')
    answer.send_keys(y)

    button1 = browser.find_element_by_xpath('.//button[@id="solve"]')
    button1.click()

finally:
    alert = browser.switch_to.alert
    text = alert.text
    print(text)
    browser.quit()
