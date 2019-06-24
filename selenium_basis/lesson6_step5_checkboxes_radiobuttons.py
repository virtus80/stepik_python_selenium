from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
y_element = browser.find_element_by_id("answer")
y_element.send_keys(y)
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()


button = browser.find_element_by_css_selector("button.btn")
button.click()
