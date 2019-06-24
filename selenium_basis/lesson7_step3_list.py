from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

num1 = int(browser.find_element_by_id("num1").text)
num2 = int(browser.find_element_by_id("num2").text)
result = str(num1+num2)

select = Select(browser.find_element_by_id("dropdown"))
select.select_by_visible_text(result)

button = browser.find_element_by_css_selector("button.btn")
button.click()
