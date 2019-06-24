import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    answer = math.log(int(time.time()))
    answer_field = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.TAG_NAME, "textarea")))
    answer_field.send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission ").click()
    feedback_field = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint")))
    feedback_message = feedback_field.text
    expected_feedback = "Correct!"
    assert feedback_message == expected_feedback, f"Expected feedback: {expected_feedback}, but actual was: {feedback_message}"