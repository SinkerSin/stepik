from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from CalcPy import calc
import time


try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    scroll = browser.find_element_by_tag_name("body").send_keys(Keys.END)
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    browser.find_element_by_tag_name("body").send_keys(Keys.END)

    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text
    x_returned = calc(x_value)

    print(x_returned)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(x_returned)

    buttonSubmit = browser.find_element_by_id("solve")
    buttonSubmit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()