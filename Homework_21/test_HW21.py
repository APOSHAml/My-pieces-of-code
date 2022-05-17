import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(15)
    yield driver
    driver.quit()


def test_products(driver):
    driver.get("http://automationpractice.com/")
    woman = driver.find_element(By.LINK_TEXT, "Women")
    woman.click()
    sort_by = Select(driver.find_element(By.ID, "selectProductSort"))
    sort_by.select_by_value("name:asc")
    elements = driver.find_elements(By.CLASS_NAME, "product-container")
    assert len(elements) == 7


def test_cart(driver):
    driver.get("http://automationpractice.com/")
    women_tab = driver.find_element(
        By.CSS_SELECTOR,
        'a[class="product_img_link"] > img[src="http://automationpractice.com/img/p/1/1-home_default.jpg"]',
    )
    ActionChains(driver).move_to_element(women_tab).perform()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-id-product="1"]'))
    ).click()
    button_check = driver.find_element(
        By.CSS_SELECTOR, 'a[class="btn btn-default button button-medium"]'
    )
    button_check.click()
    cart_check = driver.find_elements(By.CSS_SELECTOR, 'p[class="product-name"] > a')
    assert "Faded Short Sleeve T-shirts" == cart_check[1].text


def test_button(driver):
    driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-simple.html")
    button_one = driver.find_element(By.ID, "button00")
    button_one.click()
    button_two = driver.find_element(By.ID, "button01")
    button_two.click()
    button_three = driver.find_element(By.CSS_SELECTOR, 'button[id="button02"]')
    button_three.click()
    button_four = driver.find_element(By.ID, "button03")
    button_four.click()
    all_clicked = driver.find_element(By.ID, "buttonmessage")
    assert "All Buttons Clicked" in all_clicked.text


def test_button_2(driver):
    driver.get("https://testpages.herokuapp.com/styled/dynamic-buttons-disabled.html")
    start = driver.find_element(By.ID, "button00")
    start.click()
    one = driver.find_element(By.ID, "button01")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(one))
    one.click()
    two = driver.find_element(By.ID, "button02")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(two))
    two.click()
    three = driver.find_element(By.ID, "button03")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(three))
    three.click()
    all_click = driver.find_element(By.ID, "buttonmessage")
    assert "All Buttons Clicked" in all_click.text
