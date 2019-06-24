from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")
browser.find_element_by_css_selector("button.btn").click()

confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
y_element = browser.find_element_by_id("answer")
y_element.send_keys(y)

button = browser.find_element_by_css_selector("button.btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
