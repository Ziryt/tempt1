from selenium.webdriver.common.by import By

from base.elements.ElementWrapper import Button, Text, Dropdown


class DropdownPage:

    """
    Select country
    """
    text = Text(locator='//*[@class="information closable"]//strong')
    close_button = Button(locator='close_img', by=By.CLASS_NAME)
    dropdown = Dropdown(locator='//select')


