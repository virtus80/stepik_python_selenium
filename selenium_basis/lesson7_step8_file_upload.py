from selenium import webdriver
import os

browser = webdriver.Chrome()
browser.get(" http://suninjuly.github.io/file_input.html")

first_name_field = browser.find_element_by_name("firstname")
first_name_field.send_keys("Ivan")
last_name_field = browser.find_element_by_name("lastname")
last_name_field.send_keys("Petrov")
email_field = browser.find_element_by_name("email")
email_field.send_keys("ivan.petrov@gmail.com")

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'empty.txt')           # добавляем к этому пути имя файла 
file_button = browser.find_element_by_id("file")
file_button.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn")
button.click()
