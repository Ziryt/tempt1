import pytest
from base.browser.wrapper import Browser
from poms.gsqa import SliderPage
from poms.gsqa.AccordionPage import AccordionPage


@pytest.fixture
def driver():
    driver = Browser.create_instance()
    yield driver
    driver.quit()


@pytest.fixture
def accordion_page(driver):
    return AccordionPage(driver)


@pytest.fixture
def slider_page(driver):
    return SliderPage(driver)


