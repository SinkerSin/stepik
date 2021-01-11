from selenium import webdriver
import math
import time
from CalcPy import calc
from selenium.webdriver.common.keys import Keys

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button.click()

    newWindow = browser.window_handles[1]
    browser.switch_to.window(newWindow)
    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    x_returned = calc(x_value)


    answer = browser.find_element_by_id("answer")
    answer.send_keys(x_returned)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()