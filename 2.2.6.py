from selenium import webdriver
import math
import time
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    x_returned = calc(x_value)

    browser.find_element_by_tag_name('body').send_keys(Keys.END)  # или Home если наверх

    answer = browser.find_element_by_id("answer")
    answer.send_keys(x_returned)

    robotCheck = browser.find_element_by_id("robotCheckbox")
    robotCheck.click()
    robotRadio = browser.find_element_by_id("robotsRule")
    robotRadio.click()

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()