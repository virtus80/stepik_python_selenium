import time

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_button_display_for_different_languages(browser):
    browser.get(link)
    time.sleep(10)
    add_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert add_button is not None