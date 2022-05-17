from time import sleep

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("start-maximized")
    driver = Chrome(options=options)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()


def test_check_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")
    product = driver.find_element(
        By.CSS_SELECTOR, 'img[class="card-img-top img-fluid"]'
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(product).key_up(
        Keys.CONTROL
    ).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(
        By.CSS_SELECTOR, 'a[class="btn btn-success btn-lg"]'
    )
    add_to_cart.click()
    tabs1 = driver.window_handles
    driver.switch_to.window(tabs1[0])
    cart = driver.find_element(By.ID, "cartur")
    cart.click()
    element = driver.find_element(By.CLASS_NAME, "success")
    assert "Samsung galaxy s6" in element.text


def test_move(driver):
    driver.get("https://demoqa.com/menu#")
    main_item_2 = driver.find_element(By.CSS_SELECTOR, "#nav > li:nth-child(2) > a")
    ActionChains(driver).move_to_element(main_item_2).perform()
    sub_sub_list = driver.find_element(
        By.CSS_SELECTOR, "#nav > li:nth-child(2) > ul > li:nth-child(3) > a"
    )
    ActionChains(driver).move_to_element(sub_sub_list).perform()
    sub_sub_item_2 = driver.find_element(
        By.CSS_SELECTOR,
        "#nav > li:nth-child(2) > ul > li:nth-child(3) > ul > li:nth-child(2) > a",
    )
    sub_sub_item_2.click()


def test_third_task(driver):
    driver.get("https://demoqa.com/automation-practice-form")

    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Siarhei")

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Apanel")

    email_my = driver.find_element(By.ID, "userEmail")
    email_my.send_keys("aposha_18@mail.ru")

    gender = driver.find_element(By.CSS_SELECTOR, '[for="gender-radio-1"]')
    gender.click()
    sleep(0.5)

    calendar_my = driver.find_element(By.ID, "dateOfBirthInput")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(calendar_my))
    sleep(0.5)
    calendar_my.click()
    month_my = Select(
        driver.find_element(By.CLASS_NAME, "react-datepicker__month-select")
    )
    month_my.select_by_value("8")
    year_my = Select(
        driver.find_element(By.CLASS_NAME, "react-datepicker__year-select")
    )
    year_my.select_by_value("1994")
    digit_my = driver.find_element(
        By.CSS_SELECTOR, '[class="react-datepicker__day react-datepicker__day--009"]'
    )
    digit_my.click()

    hobby = driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(hobby))
    sleep(0.5)
    hobby.click()

    upload_file = driver.find_element(By.ID, "uploadPicture")
    upload_file.send_keys(
        "C:\QAP-05\personal_dirs\\apanel_siarhei\Homework_22\\testing.png"
    )

    address = driver.find_element(By.ID, "currentAddress")
    address.send_keys("Minsk, Zavodskoy")

    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("3752561274")

    ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    strings_list = [
        "Siarhei Apanel",
        "aposha_18@mail.ru",
        "3752561274",
        "09 September,1994",
        "Sports",
        "testing.png",
        "Minsk, Zavodskoy",
    ]
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "tbody"), "Student Name")
    )
    assert all(
        x in driver.find_element(By.TAG_NAME, "tbody").text for x in strings_list
    )
