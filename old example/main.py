import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


#"//div[@class="alert-danfer"]/p"
options = Options()

browser = Chrome(options=options)
browser.implicitly_wait(10)
browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
contact = browser.find_element(By.PARTIAL_LINK_TEXT, "Contact")
print(contact.get_attribute("innerText"))
val = contact.value_of_css_property('line-height')
assert "18px" in val
search = browser.find_element(By.ID, "search_query_top")
search.send_keys("lsdlsldl")
sleep(2)
search.clear()
sleep(2)

def sign(browser):
    browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    email_dr = browser.find_element(By.ID, "email_create")
    email_dr.send_keys("232323")
    email_dr.submit()

def displayed(browser):
    browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    email_dr = browser.find_element(By.CLASS_NAME, "navigation_page")
    print(email_dr.is_displayed())


def checkbox(browser):
    browser.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    chec = browser.find_element(By.NAME, "layred_category_4")
    print(chec.is_selected())
    sleep(1)
    chec.click()
    print((chec.is_selected()))

def shadow(browser):
    browser.get("http://automationpractice.com/index.php?id_category=3&controller=category")
    butt = browser.find_element(By.CLASS_NAME, "add_to_compare")
    butt.click()
    green_but = browser.find_element(By.CLASS_NAME, "bt_compare")
    print(green_but.is_enabled())
    sleep(1)
    butt.click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            green_but
        )
    )
    sleep(0.5)
    print(green_but.is_enabled())


def cart(browser):
    browser.get("http://automationpractice.com/index.php?id_category=3&controller=category")
    eye = browser.find_elements(By.CSS_SELECTOR, "i[class='icon-eye-open']")
    eye.click()
    close = browser.find_element(By.CSS_SELECTOR, "a[title='close']")
    close.click()

def selection(browser):
    browser.get("http://automationpractice.com/index.php?controller=contact")
    sel = Select(browser.find_element(By.ID, "id_contact"))
    sel.select_by_value('1')
    print(browser.get_cookies())
    browser.add_cookie({"name": "foo", "value": "bar"})
    sleep(2)
    print(browser.get_cookies())


def cookies(browser):
    browser.get("http://automationpractice.com/index.php?controller=contact")
    cok = Select(browser.find_element(By.ID, "id_contact"))
    cok.select_by_value('1')

def contac_us(browser):
    browser.get("http://automationpractice.com/index.php?controller=contact")
    text_cont = browser.find_element(By.LINK_TEXT, "Contact us")
    print(text_cont)

    return text_cont.text

@pytest.mark.parametrize(
    "func",
    [contac_us(browser)]
)
def test_contact(func):

    assert "Contact us" in func, "NNNNNNNOOOOOOO"
    sleep(5)
    browser.quit()
















# if "__name__" == __main__:
#
# test_contact(contac_us(browser))



