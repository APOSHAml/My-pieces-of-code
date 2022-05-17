import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.implicitly_wait(10)
    sleep(2)
    driver.quit()

def test_slide(driver):
    driver.get('https://demoblaze.com/index.html')
    first = driver.find_element(By.CLASS_NAME, 'carousel-control-next-icon')
    second= driver.find_element(By.CSS_SELECTOR, 'div[class="carousel-item active"]').find_element(By.TAG_NAME, 'img').get_attribute('src')
    print(first)
    assert first != second

def test_third(driver):
    driver.get('https://demoblaze.com/index.html')
    goods = driver.find_elements(By.CLASS_NAME, 'hrefch')
    text_before = goods[2].text
    title = driver.find_element(By.TAG_NAME, 'h2').text
    assert title != text_before
    butt_cart = driver.find_element(By.CLASS_NAME, 'btn btn-success btn-lg')
    butt_cart.click()
    Alert(driver).accept()
    cart_nav = driver.find_element(By.ID, 'cartur')
    cart_nav.click()
    product = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert title == product.text



def test_next(driver):
    driver.get('https://demoblaze.com/index.html')
    next_butt = driver.find_element(By.ID, 'next2')
    goods_before = driver.find_elements(By.CLASS_NAME, 'hrefch')
    goods_before_text = [x.text for x in goods_before]
    sleep(2)
    next_butt.click()
    sleep(2)
    goods_after = driver.find_elements(By.CLASS_NAME, 'hrefch')
    for good in goods_before_text:
        for g in goods_after:
            if good == g.text:
                print(good, g.text)


def test_frame(driver):
    driver.get('http://automationpractice.com/index.php?id_category=3&controller=category')
    eye = driver.find_element(By.CSS_SELECTOR, 'i[class="icon-eye-open"]')
    eye.click()
    sleep(5)
    iframe = driver.find_element(By.CSS_SELECTOR, 'iframe[class="fancybox-iframe"]')
    driver.switch_to.frame(iframe)
    add_but = driver.find_element(By.CSS_SELECTOR, 'button[class=["exclusive"]')
    add_but.click()
    driver.switch_to.default_content()
    close_but = driver.find_element(By.CSS_SELECTOR, 'span[title="Close windows"]')
    close_but.click()

def test_action(driver):
    driver.get('https://demoqa.com/buttons')
    dc = driver.find_element(By.ID, 'doubleClickBtn')
    ActionChains(driver).double_click(dc).perform()
    assert "You have done a double click" in driver.find_element(By.ID, 'doubleClickMessage').text
    rc = driver.find_element(By.ID, 'rightClickBtn')
    ActionChains(driver).context_click(rc).perform()
    assert "You have done a right click" in driver.find_element(By.ID, 'rightClickMessage').text
    cl = driver.find_elements(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')[2]
    cl.click()

def test_drg_drop(driver):
    driver.get('https://demoqa.com/droppable')
    left = driver.find_element(By.ID, 'draggable')
    right = driver.find_element(By.ID, 'droppable')
    ActionChains(driver).drag_and_drop(left, right).perform()

def test_vkladka(driver):
    driver.get('https://teachmeskills.by/')
    course = driver.find_element(By.CSS_SELECTOR, '#nav131755476 > div > div.t228__centerside > div > ul > li:nth-child(1) > a')
    ActionChains(driver).key_down(Keys.CONTROL).click(course).key_up(Keys.CONTROL).perform()
    blog = driver.find_element(By.CSS_SELECTOR, '#nav131755476 > div > div.t228__centerside > div > ul > li:nth-child(2) > a')
    ActionChains(driver).key_down(Keys.CONTROL).click(blog).key_up(Keys.CONTROL).perform()
    assert len(driver.window_handles) == 3

def test_alert(driver):
    driver.get('https://demoqa.com/alerts')
    al_butt = driver.find_element(By.ID, 'confirmButton')
    al_butt.click()
    Alert(driver).accept()
    # Alert(driver).dismiss()
    # Alert(driver).text
    driver.save_screenshot('/home/user/pakhomov/lesson 18/QAP-05/personal_dirs/yaroslav_belaychuk/Work_19/screen.png')
    sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upl = driver.find_element(By.ID, 'file-upload')
    upl.send_keys('/home/user/pakhomov/lesson 18/QAP-05/personal_dirs/yaroslav_belaychuk/Work_19/screen.png')
    sleep(3)
    driver.find_element(By.ID, 'file-submit').click()


def test_selected(driver):
    driver.get('https://demoqa.com/selectable')
    sel1 = driver.find_element(By.CSS_SELECTOR, '#verticalListContainer > li:nth-child(1)')
    sel1.click()
    sel_post = driver.find_element(By.CSS_SELECTOR, '#verticalListContainer > li.mt-2.list-group-item.active.list-group-item-action').get_attribute('class')
    assert 'active' in sel_post