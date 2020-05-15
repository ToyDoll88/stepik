import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(y)

    button2 = browser.find_element_by_css_selector('button.btn')
    button2.click()

finally:
    alert = browser.switch_to.alert
    text = alert.text
    print(text)
    browser.quit()
