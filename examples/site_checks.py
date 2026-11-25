"""Example tests called by main() in test_harness.py."""

from selenium.webdriver.common.by import By


def test_title(driver, url):
    assert driver.current_url.rstrip("/") == url.rstrip("/")
    assert driver.title == "Example Domain"


def test_heading(driver, url):
    assert driver.find_element(By.TAG_NAME, "h1").text == "Example Domain"
