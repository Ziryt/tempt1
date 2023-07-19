import pytest
from base.browser.DriverManager import DriverManager


@pytest.fixture
def driver():
    driver = DriverManager.get_wrapper()
    driver.set_position(-1000, 0)
    driver.maximize_window()
    yield driver
    driver.quit()
    DriverManager.remove_wrapper()

