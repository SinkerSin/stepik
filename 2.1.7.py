from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_tag_name("img")
    x_value = x_element.get_attribute("valuex")

    y = calc(x_value)

    Answer = browser.find_element_by_id("answer")
    Answer.send_keys(y)

    notRobot = browser.find_element_by_id("robotCheckbox")
    notRobot.click()

    rulesRobot = browser.find_element_by_id("robotsRule")
    rulesRobot.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()