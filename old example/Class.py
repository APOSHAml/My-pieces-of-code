import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = Chrome(options=options)

    driver.implicitly_wait(10)
    yield driver
    sleep(3)
    driver.quit()

def test_elements(driver):
    driver.get('https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-na-python-online')
    lesson = driver.find_elements(By.CSS_SELECTOR, 'div[class="t517__col t-col t-col_4"]')
    print(lesson)
    for les in lesson:
        if "2.Репозитории" in les.find_element(By.TAG_NAME, 'strong').text:
            assert 'Github' in les.text


def test_cont(driver):
    driver.get('http://automationpractice.com/index.php?controller=contact')
    forma = driver.find_element(By.ID, 'center_column')
    message = forma.find_element(By.CSS_SELECTOR, 'div[class="form-group"]')
    messages = forma.find_elements(By.CSS_SELECTOR, 'div[class="form-group"]')
    messages1 = driver.find_elements(By.CSS_SELECTOR, 'div[class="form-group"]')
    print(len(messages))
    print(len(messages1))
    print(message.text)


def test_tabs(driver):
    driver.get('https://the-internet.herokuapp.com/windows')
    link = driver.find_element(By.LINK_TEXT, 'Click Here')
    link.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    driver.close()
    sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    link.click()


def test_blog(driver):
    driver.get('https://teachmeskills.by/')
    blog = driver.find_elements(By.CSS_SELECTOR, 'div[class="t420__title t-name t-name_xs"]')
    for link in blog:
        assert "https://teachmeskills.by/blog" in link.find_element(By.TAG_NAME, 'href').text
        assert "https://teachmeskills.by/blog" in link.text


def test_query(driver):
    driver.get('https://the-internet.herokuapp.com/jqueryui')
    box = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/ul/li/a')
    box.click()
    enabled = driver.find_element(By.ID, 'ui-id-3')
    enabled.click()
    back = driver.find_element(By.ID, 'ui-id-8')
    back.click()
    menu = driver.find_element(By.CLASS_NAME, "example")
    assert 'JQuery UI' in menu.text


def test_gap(driver):
    driver.get('https://react-shopping-cart-67954.firebaseapp.com/')
    def gap_button():
        gapman = driver.find_element(By.CLASS_NAME, 'khMkrQ')
        return gapman.find_element(By.TAG_NAME, 'button')

    gap_button().click()
    sizes = driver.find_elements(By.CSS_SELECTOR, 'div[class="sc-eCImPb dSkwRa"]')
    sizes[0].click()
    sleep(2)
    sizes[1].click()
    sleep(2)
    gap_button().click()


def test_remove(driver):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    add.click()
    sleep(2)
    delet = driver.find_element(By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
    delet.click()
    assert element_disappeared(delet)


def element_disappeared(element):
    try:
        element.is_displayed()
    except (StaleElementReferenceException, NoSuchElementException):
        return True
    return False