from selenium.webdriver.common.by import By

from base.elements.elementWrapper import Button, Text, Dropdown
from poms.BasePage import BasePage


class DropdownPage(BasePage):

    """
    Select country
    """
    text = Text(locator='//*[@class="information closable"]//strong')
    close_button = Button(locator='close_img', by=By.CLASS_NAME)
    dropdown = Dropdown(locator='//select')


