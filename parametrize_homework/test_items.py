import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_display_for_different_languages(browser):
    browser.get(link)
    add_button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert add_button is not None