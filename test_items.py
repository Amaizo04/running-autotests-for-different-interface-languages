import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_basket_button(browser):
    browser.get(link)
    time.sleep(7)
    button = browser.find_element_by_css_selector("form#add_to_basket_form button")
    assert button == button, "Button not found"