from selenium.webdriver.common.by import By

from base.elements.elementWrapper import Button, Text, Frame
from poms.BasePage import BasePage


class DialogPage(BasePage):

    """
    Simple Accordion
    """
    ib_button = Button(locator='Color Picker', by=By.ID)
    ib_text = Text(locator='//*[@aria-labelledby="tab_item-0"]/div')
    ib_iframe = Frame(locator='//*[contains(@data-src,"image")]')

    """
    Simple Accordion
    """
    vb_button = Button(locator='Range', by=By.ID)
    vb_text = Text(locator='//*[@aria-labelledby="tab_item-1"]/div')
    vb_iframe = Frame(locator='//*[contains(@data-src,"video")]')

    """
    Simple Accordion
    """
    fb_button = Button(locator='Steps', by=By.ID)
    fb_text = Text(locator='//*[@aria-labelledby="tab_item-2"]/div')
    fb_iframe = Frame(locator='//*[contains(@data-src,"form")]')
