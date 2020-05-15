from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath(".//button[@type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_xpath('.//span[@id="input_value"]').text
    y = calc(x)
    answer = browser.find_element_by_xpath('.//input[@id="answer"]')
    answer.send_keys(y)

    button1 = browser.find_element_by_xpath('.//button[@type="submit"]')
    button1.click()

finally:
    alert = browser.switch_to.alert
    text = alert.text
    print(text)
    time.sleep(5)
    browser.quit()


