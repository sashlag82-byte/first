from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.close()


def test_open_s6(browser):
    browser.get("https://demoblaze.com/index.html")
    galaxy_s6=browser.find_element(By.LINK_TEXT, 'Samsung galaxy s6')
    galaxy_s6.click()
    title=browser.find_element(By.CSS_SELECTOR, 'h2')
    assert title.text=='Samsung galaxy s6'

def test_two_monitors(browser):
    browser.get("https://demoblaze.com/index.html")
    monitor_link = browser.find_element(By.CSS_SELECTOR, 'a.list-group-item:nth-child(4)')
    monitor_link.click()
    time.sleep(2)
    monitors=browser.find_elements(By.CSS_SELECTOR, '.card')
    assert len(monitors)==2

