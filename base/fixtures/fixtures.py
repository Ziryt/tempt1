import pytest
from base.browser.Wrapper import Browser
from poms.gsqa import SliderPage
from poms.gsqa.AccordionPage import AccordionPage


@pytest.fixture
def driver():
    driver = Browser.create_instance()
    driver.set_window_position(-1000, 0)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def accordion_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/accordion-and-tabs/')
    return AccordionPage()


@pytest.fixture
def slider_page(driver):
    driver.get('https://www.globalsqa.com/demo-site/sliders/')
    return SliderPage()


