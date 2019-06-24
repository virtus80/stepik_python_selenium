from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):

    def fill_login_form(self, browser):
        # Ваш код, который заполняет обязательные поля
        first_name_field = browser.find_element_by_css_selector("div.first_block .first")
        first_name_field.send_keys("Ivan")
        last_name_field = browser.find_element_by_css_selector("div.first_block .second")
        last_name_field.send_keys("Petrov")
        email_field = browser.find_element_by_css_selector("div.first_block .third")
        email_field.send_keys("ivan.petrov@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        self.fill_login_form(browser)
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        self.fill_login_form(browser)
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Поздравляем! Вы успешно зарегистировались!", welcome_text)

if __name__ == "__main__":
    unittest.main()
