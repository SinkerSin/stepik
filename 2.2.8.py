from selenium import webdriver
import time
import os


try:

   link = "http://suninjuly.github.io/file_input.html"
   browser = webdriver.Chrome()
   browser.get(link)

   fName = browser.find_element_by_css_selector(".form-group .form-control:nth-child(2)")
   fName.send_keys("123")
   sname = browser.find_element_by_css_selector(".form-group .form-control:nth-child(4)")
   sname.send_keys("123")
   email = browser.find_element_by_css_selector(".form-group .form-control:nth-child(6)")
   email.send_keys("123")

   file = browser.find_element_by_id("file")
   current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
   file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла
   file.send_keys(file_path)

   button = browser.find_element_by_css_selector(".btn.btn-primary")
   button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()