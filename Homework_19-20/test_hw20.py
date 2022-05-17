import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get("http://automationpractice.com")
    yield driver
    driver.quit()


def test_text_at_down(driver):
    text = driver.find_element(By.CLASS_NAME, "bottom-footer")
    assert text.text == "© 2014 Ecommerce software by PrestaShop™", "Invalid text"


def test_logo(driver):
    woman = driver.find_element(By.LINK_TEXT, "Women")
    woman.click()
    logo_on_woman = driver.find_element(By.ID, "header_logo")
    assert logo_on_woman.is_displayed()
    dresses = driver.find_element(
        By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(2) > a"
    )
    dresses.click()
    logo_on_dresses = driver.find_element(By.ID, "header_logo")
    assert logo_on_dresses.is_displayed()
    t_shirts = driver.find_element(
        By.CSS_SELECTOR, "#block_top_menu > ul > li:nth-child(3) > a"
    )
    t_shirts.click()
    logo_on_t_shirts = driver.find_element(By.ID, "header_logo")
    assert logo_on_t_shirts.is_displayed()


def test_invalid_mail(driver):
    sign = driver.find_element(By.CLASS_NAME, "login")
    sign.click()
    inputing = driver.find_element(By.ID, "email_create")
    inputing.send_keys("мыло")
    button = driver.find_element(By.ID, "SubmitCreate")
    button.click()
    error = driver.find_element(By.CSS_SELECTOR, "#create_account_error > ol > li")
    assert error.text == "Invalid email address.", "wrong text"


def test_sort_product(driver):
    woman = driver.find_element(By.LINK_TEXT, "Women")
    woman.click()
    sort_by = Select(driver.find_element(By.ID, "selectProductSort"))
    sort_by.select_by_value("name:asc")
    showing = driver.find_element(
        By.CSS_SELECTOR,
        "#center_column > div.content_sortPagiBar.clearfix > div.top-pagination-content.clearfix > div.product-count",
    )
    assert showing.text == "Showing 1 - 7 of 7 items", "Wrong text"


def test_green_background(driver):
    cart = driver.find_element(By.CSS_SELECTOR, "a[title='View my shopping cart']")
    cart.click()
    rgba = driver.find_element(
        By.CSS_SELECTOR, "#order_step > li.step_current.first > span"
    ).value_of_css_property("border-color")
    assert "rgb(115, 202, 119) rgb(116, 199, 118) rgb(116, 193, 117)" == rgba

    # r, g, b, alpha = literal_eval(rgba.strip("rgba"))
    # hex_value = "#%02x%02x%02x" % (r, g, b)
    # if not hex_value == "#73ca77":
    #     raise Exception("Button color-top is uncorrected")
